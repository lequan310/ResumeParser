from pydantic import BaseModel
from typing import Optional


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
    name: str
    email: str
    phone: str
    linkedin: Optional[str]
    latest_education: Education
    work_experiences: Optional[list[WorkExperience]]
    projects: Optional[list[Project]]
    skills: list[str]
    certifications: Optional[list[str]]


# # For Gemini API
# resume_schema = {
#     "type": "object",
#     "properties": {
#         "Education": {
#             "type": "array",
#             "items": {
#                 "type": "object",
#                 "properties": {
#                     "degree": {"type": "string"},
#                     "major": {"type": "string"},
#                     "school": {"type": "string"},
#                     "location": {"type": "string"},
#                     "start date": {"type": "string"},
#                     "end date": {"type": "string"},
#                 },
#             },
#         },
#         "Work Experience": {
#             "type": "array",
#             "items": {
#                 "type": "object",
#                 "properties": {
#                     "job title": {"type": "string"},
#                     "company": {"type": "string"},
#                     "location": {"type": "string"},
#                     "start date": {"type": "string"},
#                     "end date": {"type": "string"},
#                     "description": {"type": "string"},
#                 },
#             },
#         },
#         "Project": {
#             "type": "array",
#             "items": {
#                 "type": "object",
#                 "properties": {
#                     "name": {"type": "string"},
#                     "description": {"type": "string"},
#                     "start date": {"type": "string"},
#                     "end date": {"type": "string"},
#                     "link": {"type": "string"},
#                 },
#             },
#         },
#         "name": {"type": "string"},
#         "email": {"type": "string"},
#         "phone": {"type": "string"},
#         "skills": {"type": "array", "items": {"type": "string"}},
#         "certifications": {"type": "array", "items": {"type": "string"}},
#     },
#     "required": ["name", "email", "phone", "skills"],
# }
