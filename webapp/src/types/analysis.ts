export interface RequirementChecks {
    requirement: string;
    thinking: string;
    is_present: string;
}

export interface Analysis {
    basic_requirement_checks: RequirementChecks[];
    preferred_requirement_checks: RequirementChecks[];
}
