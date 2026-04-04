from typing import Optional

from pydantic import BaseModel


class PersonalInformation(BaseModel):
    name: str
    email: str
    phone: str
    linkedin: Optional[str]


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
    link: Optional[list[str]]


class Resume(BaseModel):
    personal_information: PersonalInformation
    latest_education: Education
    work_experiences: Optional[list[WorkExperience]]
    projects: Optional[list[Project]]
    skills: list[str]
    certifications: Optional[list[str]]
