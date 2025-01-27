from copy import deepcopy
from core.models.resume import Resume


def resolve_ref(ref: str, defs: dict) -> dict:
    """Resolve a $ref to its corresponding definition in defs."""
    ref_key = ref.split("/")[-1]
    return deepcopy(defs.get(ref_key, {}))


def process_properties(properties: dict, defs: dict) -> dict:
    """Process properties of a schema. Currently process into Gemini-supported format."""
    required = set()
    for key, value in properties.items():
        if "title" in value:
            value.pop("title")

        if "anyOf" in value:
            value = value["anyOf"][0]
        else:
            required.add(key)

        if "$ref" in value:
            ref_schema = resolve_ref(value["$ref"], defs)
            props, reqs = process_properties(ref_schema.get("properties", {}), defs)
            value = {
                "type": "object",
                "properties": props,
                "required": reqs,
            }
        elif value.get("type") == "array":
            value["items"] = process_array(value["items"], defs)
        properties[key] = value
    return properties, list(required)


def process_array(array: dict, defs: dict) -> dict:
    """Process items in an array schema."""
    if "anyOf" in array:
        array = array["anyOf"][0]

    if "$ref" in array:
        ref_schema = resolve_ref(array["$ref"], defs)
        properties, required = process_properties(
            ref_schema.get("properties", {}), defs
        )
        array = {
            "type": "object",
            "properties": properties,
            "required": required,
        }
    elif array.get("type") == "array":
        array["items"] = process_array(array["items"], defs)

    return array


def pydantic_to_schema(schema: dict) -> dict:
    """Process the main schema."""
    schema = deepcopy(schema)
    schema.pop("title", "")
    defs = schema.pop("$defs", {})

    if "properties" in schema:
        properties, required = process_properties(schema["properties"], defs)
        schema["properties"], schema["required"] = properties, required

    return schema
