import FormInput from "@/components/resume-form/FormInput";

const ResumeForm = () => {
  return (
    <div className="h-full p-6">
      <div className="space-y-12">
        {/* Personal Information */}
        <section>
          <h2 className="text-2xl font-bold mb-4 text-gray-100">
            Personal Information
          </h2>
          <div className="grid grid-cols-2 gap-4">
            <FormInput label="Name*" placeholder="John Doe" />
            <FormInput label="Email*" placeholder="john@example.com" />
            <FormInput label="Phone*" placeholder="+1 234 567 890" />
            <FormInput label="LinkedIn" placeholder="linkedin.com/in/johndoe" />
          </div>
        </section>

        {/* Education */}
        <section>
          <h2 className="text-2xl font-bold mb-4 text-gray-100">Education</h2>
          <div className="grid grid-cols-2 gap-4">
            <FormInput label="Degree" placeholder="Bachelor of Science" />
            <FormInput label="Major" placeholder="Computer Science" />
            <FormInput label="School" placeholder="University Name" />
            <FormInput label="Location" placeholder="City, Country" />
            <FormInput label="Start Date" placeholder="MM/YYYY" />
            <FormInput label="End Date" placeholder="MM/YYYY" />
          </div>
        </section>

        {/* Work Experience */}
        <section>
          <h2 className="text-2xl font-bold mb-4 text-gray-100">
            Work Experience
          </h2>
          <div className="grid grid-cols-2 gap-4">
            <FormInput label="Title" placeholder="Software Engineer" />
            <FormInput label="Company" placeholder="Company Name" />
            <FormInput label="Location" placeholder="City, Country" />
            <FormInput label="Start Date" placeholder="MM/YYYY" />
            <FormInput label="End Date" placeholder="MM/YYYY" />
            <FormInput label="Duration" placeholder="1 Year 6 Months" />
          </div>
        </section>

        {/* Projects */}
        <section>
          <h2 className="text-2xl font-bold mb-4 text-gray-100">Projects</h2>
          <div className="grid grid-cols-2 gap-4">
            <FormInput label="Name" placeholder="Personal Portfolio" />
            <FormInput label="Link" placeholder="https://johndoe.com" />
            <FormInput label="Start Date" placeholder="MM/YYYY" />
            <FormInput label="End Date" placeholder="MM/YYYY" />
          </div>
          <div className="mt-4">
            <FormInput
              label="Description"
              placeholder="Project Description and Responsibilities"
              multiline
            />
          </div>
        </section>

        {/* Certifications */}
        <section>
          <h2 className="text-2xl font-bold mb-4 text-gray-100">
            Certifications
          </h2>
          <div className="grid grid-cols-1 gap-4">
            <FormInput placeholder="AWS Certified Cloud Practitioner Certification" />
          </div>
        </section>

        {/* Skills */}
        <section>
          <h2 className="text-2xl font-bold mb-4 text-gray-100">Skills</h2>
          <div className="grid grid-cols-1 gap-4">
            <FormInput placeholder="Python, JavaScript, React..." multiline />
          </div>
        </section>
      </div>

      <div className="flex justify-center pt-12" />
    </div>
  );
};

export default ResumeForm;
