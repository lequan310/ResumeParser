from pydantic import BaseModel


class Education(BaseModel):
    degree: str
    major: str
    school: str
    location: str
    start_date: str
    end_date: str


class WorkExperience(BaseModel):
    title: str
    company: str
    location: str
    start_date: str
    end_date: str
    description: str


class Project(BaseModel):
    name: str
    description: str
    start_date: str
    end_date: str
    link: str


class Resume(BaseModel):
    name: str
    email: str
    phone: str
    educations: list[Education]
    work_experiences: list[WorkExperience]
    projects: list[Project]
    skills: list[str]
    certifications: list[str]
