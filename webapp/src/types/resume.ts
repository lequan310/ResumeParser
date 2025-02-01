export interface PersonalInformation {
    name: string;
    email: string;
    phone: string;
    linkedin?: string;
}

export interface Education {
    degree: string;
    major: string;
    school: string;
    location: string;
    startDate: string;
    endDate: string;
}

export interface WorkExperience {
    title: string;
    company: string;
    location: string;
    startDate: string;
    endDate: string;
    description: string;
}

export interface Project {
    name: string;
    description: string;
    startDate: string;
    endDate: string;
    link?: string[];
}

export interface Resume {
    personalInformation: PersonalInformation;
    latestEducation: Education;
    workExperiences?: WorkExperience[];
    projects?: Project[];
    skills: string[];
    certifications?: string[];
}
