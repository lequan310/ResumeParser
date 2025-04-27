from copy import deepcopy  # Import deepcopy for test data modification if needed
from core.utils.pydantic_to_schema import (
    resolve_ref,
    process_array,
    process_properties,
    pydantic_to_schema,
)

# --- Test Data (can be defined outside or inside the class) ---

DEFS_EXAMPLE = {
    "Address": {
        "title": "Address",
        "type": "object",
        "properties": {
            "street": {"title": "Street", "type": "string"},
            "city": {"title": "City", "type": "string"},
        },
        "required": ["street", "city"],
    },
    "StatusEnum": {
        "title": "StatusEnum",
        "enum": ["active", "inactive", "pending"],
        "type": "string",
    },
    "NestedArrayItem": {
        "title": "NestedArrayItem",
        "type": "object",
        "properties": {"id": {"title": "ID", "type": "integer"}},
        "required": ["id"],
    },
}

PROPERTIES_EXAMPLE = {
    "name": {"title": "Name", "type": "string"},
    "age": {"title": "Age", "anyOf": [{"type": "integer"}, {"type": "null"}]},
    "address": {"$ref": "#/$defs/Address"},
    "status": {"$ref": "#/$defs/StatusEnum"},
    "tags": {
        "title": "Tags",
        "type": "array",
        "items": {"type": "string"},
    },
    "history": {
        "title": "History",
        "type": "array",
        "items": {"$ref": "#/$defs/Address"},
    },
    "nested_list": {
        "title": "Nested List",
        "type": "array",
        "items": {"type": "array", "items": {"$ref": "#/$defs/NestedArrayItem"}},
    },
}

SCHEMA_EXAMPLE = {
    "title": "MainSchema",
    "type": "object",
    "properties": PROPERTIES_EXAMPLE,
    "$defs": DEFS_EXAMPLE,
}


class TestPydanticToSchema:
    # --- Tests for resolve_ref ---
    def test_resolve_ref_found(self):
        ref = "#/$defs/Address"
        expected = DEFS_EXAMPLE["Address"]
        assert resolve_ref(ref, DEFS_EXAMPLE) == expected
        assert resolve_ref(ref, DEFS_EXAMPLE) is not expected

    def test_resolve_ref_not_found(self):
        ref = "#/$defs/NonExistent"
        assert resolve_ref(ref, DEFS_EXAMPLE) == {}

    # --- Tests for process_array ---
    def test_process_array_simple(self):
        array_schema = {"type": "string"}
        assert process_array(array_schema, DEFS_EXAMPLE) == {"type": "string"}

    def test_process_array_anyof(self):
        array_schema = {"anyOf": [{"type": "integer"}, {"type": "null"}]}
        assert process_array(array_schema, DEFS_EXAMPLE) == {"type": "integer"}

    def test_process_array_ref_object(self):
        array_schema = {"$ref": "#/$defs/Address"}
        # Expected result without titles
        expected = {
            "type": "object",
            "properties": {
                "street": {"type": "string"},
                "city": {"type": "string"},
            },
            "required": ["street", "city"],  # Keep original expected order here
        }

        # Get the actual result, use deepcopy if the function modifies input
        actual = process_array(deepcopy(array_schema), DEFS_EXAMPLE)

        # --- Order-independent check for 'required' ---
        # 1. Extract 'required' lists, providing an empty list default if missing
        actual_required = actual.pop("required", [])
        expected_required = expected.pop("required", [])

        # 2. Compare the lists as sets
        assert set(actual_required) == set(expected_required)
        # --- End of order-independent check ---

        # 3. Compare the rest of the dictionaries (now without 'required')
        assert actual == expected

    def test_process_array_nested_array_ref(self):
        array_schema = {"type": "array", "items": {"$ref": "#/$defs/NestedArrayItem"}}
        expected = {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"id": {"type": "integer"}},
                "required": ["id"],
            },
        }
        assert process_array(array_schema, DEFS_EXAMPLE) == expected

    # --- Tests for process_properties ---
    def test_process_properties(self):
        # Use deepcopy because process_properties modifies the input dict
        props_copy = deepcopy(PROPERTIES_EXAMPLE)
        processed_props, required = process_properties(props_copy, DEFS_EXAMPLE)

        assert set(required) == {
            "name",
            "address",
            "status",
            "tags",
            "history",
            "nested_list",
        }
        assert "title" not in processed_props["name"]
        assert processed_props["name"]["type"] == "string"
        assert "title" not in processed_props["age"]
        assert processed_props["age"]["type"] == "integer"
        assert "title" not in processed_props["address"]
        assert processed_props["address"]["type"] == "object"
        assert "street" in processed_props["address"]["properties"]
        assert set(processed_props["address"]["required"]) == {"street", "city"}
        assert "title" not in processed_props["status"]
        assert processed_props["status"]["type"] == "string"
        assert processed_props["status"]["enum"] == ["active", "inactive", "pending"]
        assert "title" not in processed_props["tags"]
        assert processed_props["tags"]["type"] == "array"
        assert processed_props["tags"]["items"]["type"] == "string"
        assert "title" not in processed_props["history"]
        assert processed_props["history"]["type"] == "array"
        assert processed_props["history"]["items"]["type"] == "object"
        assert "street" in processed_props["history"]["items"]["properties"]
        assert set(processed_props["history"]["items"]["required"]) == {
            "street",
            "city",
        }
        assert "title" not in processed_props["nested_list"]
        assert processed_props["nested_list"]["type"] == "array"
        assert processed_props["nested_list"]["items"]["type"] == "array"
        assert processed_props["nested_list"]["items"]["items"]["type"] == "object"
        assert "id" in processed_props["nested_list"]["items"]["items"]["properties"]
        assert set(processed_props["nested_list"]["items"]["items"]["required"]) == {
            "id"
        }

    # --- Tests for pydantic_to_schema ---
    def test_pydantic_to_schema_full(self):
        # Use deepcopy because pydantic_to_schema modifies the input dict
        schema_copy = deepcopy(SCHEMA_EXAMPLE)
        processed_schema = pydantic_to_schema(schema_copy)

        assert "title" not in processed_schema
        assert "$defs" not in processed_schema
        assert "properties" in processed_schema
        assert "required" in processed_schema

        # Re-process original properties for comparison
        expected_props, expected_reqs = process_properties(
            deepcopy(SCHEMA_EXAMPLE["properties"]), SCHEMA_EXAMPLE["$defs"]
        )
        assert processed_schema["properties"] == expected_props
        assert set(processed_schema["required"]) == set(expected_reqs)

    def test_pydantic_to_schema_no_defs(self):
        schema_no_defs = {
            "title": "NoDefsSchema",
            "type": "object",
            "properties": {"simple": {"title": "Simple", "type": "string"}},
        }
        processed = pydantic_to_schema(deepcopy(schema_no_defs))
        assert "title" not in processed
        assert "$defs" not in processed
        assert processed["properties"]["simple"] == {"type": "string"}
        assert processed["required"] == ["simple"]

    def test_pydantic_to_schema_no_properties(self):
        schema_no_props = {
            "title": "NoPropsSchema",
            "type": "object",
            "$defs": DEFS_EXAMPLE,
        }
        processed = pydantic_to_schema(deepcopy(schema_no_props))
        assert "title" not in processed
        assert "$defs" not in processed
        assert "properties" not in processed
        assert "required" not in processed

    def test_pydantic_to_schema_empty(self):
        schema_empty = {}
        processed = pydantic_to_schema(deepcopy(schema_empty))
        assert processed == {}

    def test_pydantic_to_schema_preserves_other_fields(self):
        schema_extra = {
            "title": "ExtraSchema",
            "type": "object",
            "description": "Keep this description",
            "properties": {"field": {"title": "Field", "type": "boolean"}},
        }
        processed = pydantic_to_schema(deepcopy(schema_extra))
        assert "title" not in processed
        assert processed["description"] == "Keep this description"
        assert processed["properties"]["field"] == {"type": "boolean"}
        assert processed["required"] == ["field"]
