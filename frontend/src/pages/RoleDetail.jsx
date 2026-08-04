import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import api from "../api/axios";

function RoleDetail() {
  const { slug } = useParams();
  const [role, setRole] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRole = async () => {
      setLoading(true);
      setError("");
      try {
        const response = await api.get(`/roles/${slug}`);
        setRole(response.data);
      } catch (err) {
        setError("Role not found.");
      } finally {
        setLoading(false);
      }
    };
    fetchRole();
  }, [slug]);

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-900 flex items-center justify-center">
        <p className="text-white">Loading...</p>
      </div>
    );
  }

  if (error || !role) {
    return (
      <div className="min-h-screen bg-slate-900 flex flex-col items-center justify-center gap-4">
        <p className="text-red-400">{error}</p>
        <Link to="/roadmap" className="text-blue-400 hover:underline">
          ← Back to all roles
        </Link>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-900 px-4 py-10">
      <div className="max-w-3xl mx-auto">
        <Link to="/roadmap" className="text-slate-400 hover:text-white text-sm">
          ← Back to all roles
        </Link>

        <h1 className="text-3xl font-bold text-white mt-4">{role.title}</h1>
        <p className="text-blue-400 font-medium mt-1">{role.average_salary}</p>

        <section className="mt-8">
          <h2 className="text-xl font-semibold text-white mb-2">Job Description</h2>
          <p className="text-slate-300 leading-relaxed">{role.job_description}</p>
        </section>

        <section className="mt-8">
          <h2 className="text-xl font-semibold text-white mb-3">Skills Required</h2>
          <div className="flex flex-wrap gap-2">
            {role.skills_required.map((skill, i) => (
              <span key={i} className="bg-slate-800 text-slate-200 text-sm px-3 py-1 rounded-full border border-slate-700">
                {skill}
              </span>
            ))}
          </div>
        </section>

        <section className="mt-8">
          <h2 className="text-xl font-semibold text-white mb-3">Hiring Companies</h2>
          <div className="flex flex-wrap gap-2">
            {role.hiring_companies.map((company, i) => (
              <span key={i} className="bg-slate-800 text-slate-200 text-sm px-3 py-1 rounded-full border border-slate-700">
                {company}
              </span>
            ))}
          </div>
        </section>

        <section className="mt-8">
          <h2 className="text-xl font-semibold text-white mb-3">Learning Roadmap</h2>
          <ol className="space-y-2">
            {role.learning_roadmap.map((step, i) => (
              <li key={i} className="flex gap-3 text-slate-300">
                <span className="text-blue-400 font-semibold">{i + 1}.</span>
                <span>{step}</span>
              </li>
            ))}
          </ol>
        </section>

        <section className="mt-8 mb-10">
          <h2 className="text-xl font-semibold text-white mb-2">Interview Pattern</h2>
          <p className="text-slate-300 leading-relaxed">{role.interview_pattern}</p>
        </section>
      </div>
    </div>
  );
}

export default RoleDetail;