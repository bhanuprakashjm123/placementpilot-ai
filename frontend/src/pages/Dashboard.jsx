import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";

function Dashboard() {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await api.get("/auth/me");
        setUser(response.data);
      } catch (err) {
        localStorage.removeItem("token");
        navigate("/login");
      }
    };
    fetchUser();
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  if (!user) {
    return (
      <div className="min-h-screen bg-slate-900 flex items-center justify-center">
        <p className="text-white">Loading...</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-900 px-4 py-10">
      <div className="max-w-2xl mx-auto bg-slate-800 rounded-xl p-8 shadow-lg">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-2xl font-bold text-white">Dashboard</h1>
          <div className="flex gap-3 items-center">
            <button
              onClick={() => navigate("/roadmap")}
              className="bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded-lg px-4 py-2 transition"
            >
              Career Roadmap
            </button>
            <button
              onClick={handleLogout}
              className="bg-red-600 hover:bg-red-700 text-white text-sm font-medium rounded-lg px-4 py-2 transition"
            >
              Logout
            </button>
          </div>
        </div>

        <div className="space-y-2 text-slate-300">
          <p><span className="text-slate-500">Name:</span> {user.full_name}</p>
          <p><span className="text-slate-500">Email:</span> {user.email}</p>
          <p><span className="text-slate-500">Account status:</span> {user.is_active ? "Active" : "Inactive"}</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;