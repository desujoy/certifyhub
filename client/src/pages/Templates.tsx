// src/pages/Templates.tsx

import TemplateUploader from "../components/TemplateUploader";
import TemplateList from "../components/TemplateList";
import TemplateEditor from "../components/TemplateEditor";

export default function Templates({template,
  setTemplate,
}: {
  template: string;
  setTemplate: (template: string) => void;
}) {
  

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-3xl font-bold my-4">Manage Templates</h1>
      <TemplateUploader />
      <TemplateList setTemplate={setTemplate} />

       {/*{template && (
        <div className="mt-6 w-full flex flex-col items-center">
          <h2 className="text-2xl font-semibold">Edit Selected Template</h2>
          <TemplateEditor template={template} />
        </div>
      )} */}
    </div>
  );
}
