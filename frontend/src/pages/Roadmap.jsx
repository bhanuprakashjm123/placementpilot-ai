import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../api/axios";

function Roadmap() {
  const [roles, setRoles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchRoles = async () => {
      try {
        const response = await api.get("/roles");
        setRoles(response.data);
      } catch (err) {
        setError("Could not load career roles. Please try again later.");
      } finally {
        setLoading(false);
      }
    };
    fetchRoles();
  }, []);

  return (
    <div className="min-h-screen bg-slate-900 px-4 py-10">
      <div className="max-w-5xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-bold text-white">Career Roadmap</h1>
            <p className="text-slate-400 mt-1">Choose a target role to see your path.</p>
          </div>
          <button
            onClick={() => navigate("/dashboard")}
            className="text-slate-300 hover:text-white text-sm"
          >
            ← Back to Dashboard
          </button>
        </div>

        {loading && <p className="text-slate-400">Loading roles...</p>}
        {error && <p className="text-red-400">{error}</p>}

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
          {roles.map((role) => (
            <Link
              key={role.id}
              to={`/roadmap/${role.slug}`}
              className="bg-slate-800 hover:bg-slate-700 rounded-xl p-5 transition border border-slate-700"
            >
              <h2 className="text-lg font-semibold text-white mb-2">{role.title}</h2>
              <p className="text-blue-400 text-sm">{role.average_salary}</p>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Roadmap;