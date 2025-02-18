import FormInput from "@/components/resume-form/FormInput";
import { useResumeContext } from "@/hooks";

const ResumeForm = () => {
  const { resume } = useResumeContext();

  return (
    <div className="h-full p-6">
      <div className="space-y-12">
        {/* Personal Information */}
        <section>
          <h2 className="text-2xl font-bold mb-4 text-gray-100">
            Personal Information
          </h2>
          <div className="grid grid-cols-2 gap-4">
            <FormInput
              label="Name*"
              placeholder="John Doe"
              value={resume?.personal_information.name}
            />
            <FormInput
              label="Email*"
              placeholder="john@example.com"
              value={resume?.personal_information.email}
            />
            <FormInput
              label="Phone*"
              placeholder="+1 234 567 890"
              value={resume?.personal_information.phone}
            />
            <FormInput
              label="LinkedIn"
              placeholder="linkedin.com/in/johndoe"
              value={resume?.personal_information.linkedin}
            />
          </div>
        </section>

        {/* Latest Education */}
        <section>
          <h2 className="text-2xl font-bold mb-4 text-gray-100">
            Latest Education
          </h2>
          <div className="grid grid-cols-2 gap-4">
            <FormInput
              label="Degree"
              placeholder="Bachelor of Science"
              value={resume?.latest_education?.degree}
            />
            <FormInput
              label="Major"
              placeholder="Computer Science"
              value={resume?.latest_education?.major}
            />
            <FormInput
              label="School"
              placeholder="University Name"
              value={resume?.latest_education?.school}
            />
            <FormInput
              label="Location"
              placeholder="City, Country"
              value={resume?.latest_education?.location}
            />
            <FormInput
              label="Start Date"
              placeholder="MM/YYYY"
              value={resume?.latest_education?.start_date}
            />
            <FormInput
              label="End Date"
              placeholder="MM/YYYY"
              value={resume?.latest_education?.end_date}
            />
          </div>
        </section>

        {/* Work Experience */}
        <section>
          <h2 className="text-2xl font-bold mb-4 text-gray-100">
            Work Experiences
            {resume?.yoe
              ? ` (${resume.yoe.year} Years ${resume.yoe.month} Months)`
              : ""}
          </h2>
          <div className="grid gap-10">
            {resume?.work_experiences?.map((workExperience, index) => (
              <div
                className="grid grid-cols-2 gap-4"
                key={`experience-${index}`}
              >
                <FormInput
                  label="Title"
                  placeholder="Software Engineer"
                  value={workExperience.title}
                />
                <FormInput
                  label="Company"
                  placeholder="Company Name"
                  value={workExperience.company}
                />
                <FormInput
                  label="Location"
                  placeholder="City, Country"
                  value={workExperience.location}
                />
                <FormInput
                  label="Start Date"
                  placeholder="MM/YYYY"
                  value={workExperience.start_date}
                />
                <FormInput
                  label="End Date"
                  placeholder="MM/YYYY"
                  value={workExperience.end_date}
                />
                <FormInput
                  label="Duration"
                  placeholder="1 Year 6 Months"
                  value={`${workExperience.duration.year} Years ${workExperience.duration.month} Months`}
                />
              </div>
            ))}
          </div>
        </section>

        {/* Projects */}
        <section>
          <h2 className="text-2xl font-bold mb-4 text-gray-100">Projects</h2>
          <div className="grid gap-10">
            {resume?.projects?.map((project, index) => (
              <div key={`project-${index}`}>
                <div className="grid grid-cols-2 gap-4">
                  <FormInput
                    label="Name"
                    placeholder="Personal Portfolio"
                    value={project.name}
                  />
                  <FormInput
                    label="Link"
                    placeholder="https://johndoe.com"
                    value={project.link?.at(0)}
                  />
                  <FormInput
                    label="Start Date"
                    placeholder="MM/YYYY"
                    value={project.start_date}
                  />
                  <FormInput
                    label="End Date"
                    placeholder="MM/YYYY"
                    value={project.end_date}
                  />
                </div>
                <div className="mt-4">
                  <FormInput
                    label="Description"
                    placeholder="Project Description and Responsibilities"
                    multiline
                    value={project.description}
                  />
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Certifications */}
        <section>
          <h2 className="text-2xl font-bold mb-4 text-gray-100">
            Certifications
          </h2>
          <div className="grid grid-cols-1 gap-4">
            {resume?.certifications?.map((certification, index) => (
              <FormInput
                placeholder="AWS Certified Cloud Practitioner Certification"
                value={certification}
                key={index}
              />
            ))}
          </div>
        </section>

        {/* Skills */}
        <section>
          <h2 className="text-2xl font-bold mb-4 text-gray-100">Skills</h2>
          <div className="grid grid-cols-1 gap-4">
            <FormInput
              placeholder="Python, JavaScript, React..."
              multiline
              value={`${resume?.skills.join(", ") || ""}`}
            />
          </div>
        </section>
      </div>

      <div className="flex justify-center pt-12" />
    </div>
  );
};

export default ResumeForm;
