export interface PersonalInformation {
    name: string;
    email: string;
    phone: string;
    linkedin?: string;
}

export interface LatestEducation {
    degree: string;
    major: string;
    school: string;
    location: string;
    start_date: string;
    end_date: string;
}

export interface WorkExperience {
    title: string;
    company: string;
    location: string;
    duration: YOE;
    start_date: string;
    end_date: string;
    description: string;
}

export interface Project {
    name: string;
    description: string;
    start_date: string;
    end_date: string;
    link?: string[];
}

export interface YOE {
    year: number;
    month: number;
}

export interface Resume {
    personal_information: PersonalInformation;
    latest_education?: LatestEducation;
    work_experiences?: WorkExperience[];
    projects?: Project[];
    skills: string[];
    certifications?: string[];
    yoe: YOE;
}
