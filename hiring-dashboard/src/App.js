
// // // import React, { useState } from "react";
// // // import axios from "axios";

// // // function App() {
// // //   const [data, setData] = useState(null);
// // //   const [loading, setLoading] = useState(false);
// // //   const [githubUrl, setGithubUrl] = useState("");
// // //   const [role, setRole] = useState("");
// // //   const [resume, setResume] = useState(null);

// // //   const fetchAnalysis = async () => {
// // //     if (!githubUrl || !role || !resume) {
// // //       alert("Please fill all fields and upload a resume");
// // //       return;
// // //     }

// // //     try {
// // //       setLoading(true);
// // //       const formData = new FormData();
// // //       formData.append("github_url", githubUrl);
// // //       formData.append("role", role);
// // //       formData.append("resume", resume);

// // //       const response = await axios.post("http://127.0.0.1:8000/full-analysis", formData, {
// // //         headers: {
// // //           "Content-Type": "multipart/form-data",
// // //         },
// // //       });
// // //       setData(response.data);
// // //       setLoading(false);
// // //     } catch (err) {
// // //       setLoading(false);
// // //       setData({
// // //         //dummy data 
// // //         //candidateScore: 87,
// // //         skillMatch: 92,
// // //         authenticity: 85,
// // //         activityConsistency: 78,
// // //         platforms: [
// // //           { name: "LinkedIn", value: "+7.5k", trend: 139 },
// // //           { name: "GitHub", value: "+4.9k", trend: 98 },
// // //           { name: "StackOverflow", value: "+3.4k", trend: 76 },
// // //         ],
// // //         monthlyActivity: [
// // //           { month: "Jan", commits: 45 },
// // //           { month: "Feb", commits: 62 },
// // //           { month: "Mar", commits: 58 },
// // //           { month: "Apr", commits: 71 },
// // //           { month: "May", commits: 65 },
// // //           { month: "Jun", commits: 80 },
// // //         ],
// // //         genderPrediction: { male: 32, female: 68 },
// // //         recommendation: "Strong Hire",
// // //         interviewQuestions: [
// // //           "Describe your most complex system design challenge",
// // //           "Walk me through your GitHub contributions",
// // //           "How do you ensure code quality?",
// // //         ],
// // //       });
// // //     }
// // //   };

// // //   const handleFileChange = (e) => {
// // //     if (e.target.files && e.target.files[0]) {
// // //       setResume(e.target.files[0]);
// // //     }
// // //   };

// // //   return (
// // //     <div className="min-h-screen bg-gradient-to-br from-gray-900 to-black text-white p-8">
// // //       <div className="max-w-7xl mx-auto">
// // //         {/* Header */}
// // //         <div className="flex items-center justify-between mb-8">
// // //           <div className="flex items-center gap-8">
// // //             <div className="w-10 h-10 bg-white rounded-full flex items-center justify-center">
// // //               <span className="text-black font-bold">AI</span>
// // //             </div>
// // //             <nav className="flex gap-6 text-gray-400">
// // //               <button className="hover:text-white">Overview</button>
// // //               <button className="hover:text-white">Learn</button>
// // //               <button className="hover:text-white">Support</button>
// // //             </nav>
// // //           </div>
// // //         </div>

// // //         <h1 className="text-4xl font-bold mb-8">AI Hiring Intelligence Dashboard</h1>

// // //         {/* Input Section */}
// // //         <div className="bg-gray-800/50 rounded-3xl p-8 border border-gray-700 mb-8">
// // //           <h2 className="text-2xl font-bold mb-6">Candidate Analysis</h2>
// // //           <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
// // //             <div>
// // //               <label className="block text-sm text-gray-400 mb-2">GitHub URL</label>
// // //               <input
// // //                 type="text"
// // //                 value={githubUrl}
// // //                 onChange={(e) => setGithubUrl(e.target.value)}
// // //                 placeholder="https://github.com/username"
// // //                 className="w-full bg-gray-700/50 border border-gray-600 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500"
// // //               />
// // //             </div>
// // //             <div>
// // //               <label className="block text-sm text-gray-400 mb-2">Role</label>
// // //               <input
// // //                 type="text"
// // //                 value={role}
// // //                 onChange={(e) => setRole(e.target.value)}
// // //                 placeholder="e.g., Senior Backend Developer"
// // //                 className="w-full bg-gray-700/50 border border-gray-600 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500"
// // //               />
// // //             </div>
// // //             <div>
// // //               <label className="block text-sm text-gray-400 mb-2">Resume (PDF)</label>
// // //               <input
// // //                 type="file"
// // //                 accept=".pdf"
// // //                 onChange={handleFileChange}
// // //                 className="w-full bg-gray-700/50 border border-gray-600 rounded-lg px-4 py-3 text-white file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-purple-600 file:text-white hover:file:bg-purple-700 focus:outline-none focus:border-purple-500"
// // //               />
// // //             </div>
// // //           </div>
// // //           <button
// // //             onClick={fetchAnalysis}
// // //             disabled={loading}
// // //             className="w-full md:w-auto px-8 py-3 bg-gradient-to-r from-purple-600 to-pink-600 rounded-lg hover:from-purple-700 hover:to-pink-700 transition-all duration-300 shadow-lg hover:shadow-purple-500/50 font-semibold disabled:opacity-50 disabled:cursor-not-allowed"
// // //           >
// // //             {loading ? "Analyzing..." : "Analyze Candidate"}
// // //           </button>
// // //         </div>

// // //         {loading && (
// // //           <div className="flex items-center justify-center py-20">
// // //             <div className="w-16 h-16 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
// // //           </div>
// // //         )}

// // //         {!loading && data && (
// // //           <>
// // //             <h2 className="text-3xl font-bold mb-8">General statistics</h2>

// // //             {/* Main Grid */}
// // //             <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
// // //               {/* Large Card - Activity Chart */}
// // //               <div className="col-span-1 md:col-span-2 bg-gradient-to-br from-pink-200 to-purple-200 rounded-3xl p-8 relative overflow-hidden">
// // //                 <div className="text-black">
// // //                   <p className="text-sm mb-2">Candidate activity score</p>
// // //                   <h2 className="text-5xl font-bold mb-1">+{data.candidateScore}%</h2>
                  
// // //                   {/* Dot Chart */}
// // //                   <div className="mt-8 flex items-end justify-between h-32">
// // //                     {data.monthlyActivity.map((item, index) => (
// // //                       <div key={index} className="flex flex-col items-center gap-1">
// // //                         <div className="flex flex-col gap-1">
// // //                           {Array.from({ length: Math.floor(item.commits / 10) }).map((_, i) => (
// // //                             <div
// // //                               key={i}
// // //                               className={`w-3 h-3 rounded-full ${
// // //                                 i >= Math.floor(item.commits / 10) - 3 ? "bg-black" : "bg-black/20"
// // //                               }`}
// // //                             ></div>
// // //                           ))}
// // //                         </div>
// // //                         <span className="text-xs mt-2 text-black/60">{item.month}</span>
// // //                       </div>
// // //                     ))}
// // //                   </div>

// // //                   <div className="absolute top-4 right-4 flex gap-4 text-xs">
// // //                     <span className="flex items-center gap-2">
// // //                       <div className="w-3 h-3 rounded-full bg-black/20"></div>
// // //                       Without training
// // //                     </span>
// // //                     <span className="flex items-center gap-2">
// // //                       <div className="w-3 h-3 rounded-full bg-black"></div>
// // //                       With training
// // //                     </span>
// // //                   </div>
// // //                 </div>
// // //               </div>

// // //               {/* Right Column - Chat Interface */}
// // //               <div className="row-span-2 bg-gray-800/50 rounded-3xl p-6 border border-gray-700">
// // //                 <div className="flex gap-2 mb-6">
// // //                   <button className="px-4 py-2 bg-white text-black rounded-full text-sm font-medium">
// // //                     Today
// // //                   </button>
// // //                   <button className="px-4 py-2 text-gray-400 hover:text-white text-sm">
// // //                     Trends 2024
// // //                   </button>
// // //                   <button className="px-4 py-2 text-gray-400 hover:text-white text-sm">
// // //                     Total salary
// // //                   </button>
// // //                 </div>

// // //                 <div className="space-y-6 text-sm">
// // //                   <div>
// // //                     <p className="text-gray-400 mb-2">How can I help you today?</p>
// // //                     <p className="text-xs text-gray-500">11:32 AM</p>
// // //                   </div>

// // //                   <div className="bg-gray-700/50 rounded-2xl p-4">
// // //                     <p className="text-sm leading-relaxed">
// // //                       Make a prediction on how launching new AI features will impact the candidate conversion rate.
// // //                     </p>
// // //                   </div>

// // //                   <div>
// // //                     <p className="text-sm leading-relaxed mb-2">
// // //                       Of course, I will show you graphs illustrating how the launch of advertising may impact the number of conversions this year.
// // //                     </p>
// // //                     <p className="text-xs text-gray-500">11:38 AM</p>
// // //                   </div>

// // //                   <div>
// // //                     <p className="text-sm leading-relaxed">
// // //                       On the graph, you can see the percentage increase in conversions.
// // //                     </p>
// // //                   </div>

// // //                   <div>
// // //                     <p className="text-sm leading-relaxed">
// // //                       I will also show you from which platform, in my opinion, the most candidates will come.
// // //                     </p>
// // //                     <p className="text-xs text-gray-500 mt-2">11:38 AM</p>
// // //                   </div>
// // //                 </div>

// // //                 <div className="mt-6">
// // //                   <input
// // //                     type="text"
// // //                     placeholder="How can I help you?"
// // //                     className="w-full bg-gray-700/30 border border-gray-600 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-purple-500"
// // //                   />
// // //                 </div>
// // //               </div>

// // //               {/* Platform List */}
// // //               <div className="bg-gray-800/50 rounded-3xl p-6 border border-gray-700">
// // //                 <p className="text-sm text-gray-400 mb-6">List of platforms</p>
                
// // //                 <div className="space-y-4">
// // //                   {data.platforms.map((platform, index) => (
// // //                     <div key={index} className="flex items-center justify-between">
// // //                       <span className="text-white">{platform.name}</span>
// // //                       <span className="text-green-400 font-medium">{platform.value}</span>
// // //                     </div>
// // //                   ))}
// // //                 </div>

// // //                 <button className="mt-6 px-4 py-2 text-sm text-gray-400 hover:text-white flex items-center gap-2">
// // //                   +2 more
// // //                   <span className="px-3 py-1 border border-gray-600 rounded-full text-xs">
// // //                     View all
// // //                   </span>
// // //                 </button>
// // //               </div>

// // //               {/* Top Platform Card */}
// // //               <div className="bg-gray-800/50 rounded-3xl p-6 border border-gray-700">
// // //                 <p className="text-sm text-gray-400 mb-4">GitHub - the most active platform</p>
// // //                 <h3 className="text-4xl font-bold mb-2">+139%</h3>
                
// // //                 <div className="flex gap-1 mt-4">
// // //                   {Array.from({ length: 20 }).map((_, i) => (
// // //                     <div
// // //                       key={i}
// // //                       className={`w-1 rounded-full ${
// // //                         i < 14 ? "h-6 bg-white" : "h-3 bg-gray-600"
// // //                       }`}
// // //                     ></div>
// // //                   ))}
// // //                 </div>
// // //               </div>

// // //               {/* Gender Prediction */}
// // //               <div className="bg-gray-800/50 rounded-3xl p-6 border border-gray-700">
// // //                 <p className="text-sm text-gray-400 mb-4">Predicted gender of clients</p>
                
// // //                 <div className="flex items-end gap-8">
// // //                   <div>
// // //                     <p className="text-3xl font-bold mb-1">{data.genderPrediction.male}%</p>
// // //                     <p className="text-xs text-gray-400">male</p>
// // //                   </div>
// // //                   <div>
// // //                     <p className="text-3xl font-bold mb-1">{data.genderPrediction.female}%</p>
// // //                     <p className="text-xs text-gray-400">female</p>
// // //                   </div>
// // //                 </div>
// // //               </div>
// // //             </div>
// // //           </>
// // //         )}

// // //         {!loading && !data && (
// // //           <div className="text-center py-20">
// // //             <p className="text-gray-400 text-lg">Enter candidate details above to start analysis</p>
// // //           </div>
// // //         )}
// // //       </div>
// // //     </div>
// // //   );
// // // }

// // // export default App;


// // import React, { useState } from "react";
// // import axios from "axios";

// // function App() {
// //   const [data, setData] = useState(null);
// //   const [loading, setLoading] = useState(false);
// //   const [githubUsername, setGithubUsername] = useState("");
// //   const [linkedinUrl, setLinkedinUrl] = useState("");
// //   const [role, setRole] = useState("");
// //   const [resume, setResume] = useState(null);
// //   const [error, setError] = useState("");

// //   const fetchAnalysis = async () => {
// //     if (!githubUsername || !linkedinUrl || !role || !resume) {
// //       setError("Please fill all fields and upload a resume");
// //       return;
// //     }

// //     try {
// //       setLoading(true);
// //       setError("");
      
// //       const formData = new FormData();
// //       formData.append("resume", resume);

// //       const response = await axios.post(
// //         `http://127.0.0.1:8000/full-analysis?github_username=${encodeURIComponent(githubUsername)}&linkedin_url=${encodeURIComponent(linkedinUrl)}&role=${encodeURIComponent(role)}`,
// //         formData,
// //         {
// //           headers: {
// //             "Content-Type": "multipart/form-data",
// //           },
// //         }
// //       );
      
// //       setData(response.data);
// //       setLoading(false);
// //     } catch (err) {
// //       setLoading(false);
// //       setError(err.response?.data?.detail || "Analysis failed. Please try again.");
// //       console.error("Error:", err);
// //     }
// //   };

// //   const handleFileChange = (e) => {
// //     if (e.target.files && e.target.files[0]) {
// //       setResume(e.target.files[0]);
// //       setError("");
// //     }
// //   };

// //   return (
// //     <div className="min-h-screen bg-gradient-to-br from-gray-900 to-black text-white p-8">
// //       <div className="max-w-7xl mx-auto">
// //         {/* Header */}
// //         <div className="flex items-center justify-between mb-8">
// //           <div className="flex items-center gap-8">
// //             <div className="w-10 h-10 bg-white rounded-full flex items-center justify-center">
// //               <span className="text-black font-bold">AI</span>
// //             </div>
// //             <nav className="flex gap-6 text-gray-400">
// //               <button className="hover:text-white">Overview</button>
// //               <button className="hover:text-white">Learn</button>
// //               <button className="hover:text-white">Support</button>
// //             </nav>
// //           </div>
// //         </div>

// //         <h1 className="text-4xl font-bold mb-8">AI Hiring Intelligence Dashboard</h1>

// //         {/* Input Section */}
// //         <div className="bg-gray-800/50 rounded-3xl p-8 border border-gray-700 mb-8">
// //           <h2 className="text-2xl font-bold mb-6">Candidate Analysis</h2>
          
// //           {error && (
// //             <div className="mb-6 p-4 bg-red-500/20 border border-red-500 rounded-lg text-red-300">
// //               {error}
// //             </div>
// //           )}
          
// //           <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
// //             <div>
// //               <label className="block text-sm text-gray-400 mb-2">GitHub Username</label>
// //               <input
// //                 type="text"
// //                 value={githubUsername}
// //                 onChange={(e) => setGithubUsername(e.target.value)}
// //                 placeholder="e.g., octocat"
// //                 className="w-full bg-gray-700/50 border border-gray-600 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500"
// //               />
// //             </div>
// //             <div>
// //               <label className="block text-sm text-gray-400 mb-2">LinkedIn URL</label>
// //               <input
// //                 type="text"
// //                 value={linkedinUrl}
// //                 onChange={(e) => setLinkedinUrl(e.target.value)}
// //                 placeholder="https://linkedin.com/in/username"
// //                 className="w-full bg-gray-700/50 border border-gray-600 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500"
// //               />
// //             </div>
// //             <div>
// //               <label className="block text-sm text-gray-400 mb-2">Role</label>
// //               <input
// //                 type="text"
// //                 value={role}
// //                 onChange={(e) => setRole(e.target.value)}
// //                 placeholder="e.g., Senior Backend Developer"
// //                 className="w-full bg-gray-700/50 border border-gray-600 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500"
// //               />
// //             </div>
// //             <div>
// //               <label className="block text-sm text-gray-400 mb-2">Resume (PDF)</label>
// //               <input
// //                 type="file"
// //                 accept=".pdf"
// //                 onChange={handleFileChange}
// //                 className="w-full bg-gray-700/50 border border-gray-600 rounded-lg px-4 py-3 text-white file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-purple-600 file:text-white hover:file:bg-purple-700 focus:outline-none focus:border-purple-500"
// //               />
// //               {resume && (
// //                 <p className="text-xs text-green-400 mt-2">✓ {resume.name}</p>
// //               )}
// //             </div>
// //           </div>
// //           <button
// //             onClick={fetchAnalysis}
// //             disabled={loading}
// //             className="w-full md:w-auto px-8 py-3 bg-gradient-to-r from-purple-600 to-pink-600 rounded-lg hover:from-purple-700 hover:to-pink-700 transition-all duration-300 shadow-lg hover:shadow-purple-500/50 font-semibold disabled:opacity-50 disabled:cursor-not-allowed"
// //           >
// //             {loading ? "Analyzing..." : "Analyze Candidate"}
// //           </button>
// //         </div>

// //         {loading && (
// //           <div className="flex flex-col items-center justify-center py-20">
// //             <div className="w-16 h-16 border-4 border-purple-500 border-t-transparent rounded-full animate-spin mb-4"></div>
// //             <p className="text-gray-400">Analyzing resume, GitHub, and LinkedIn profiles...</p>
// //           </div>
// //         )}

// //         {!loading && data && (
// //           <>
// //             <h2 className="text-3xl font-bold mb-8">Analysis Results</h2>

// //             {/* Score Cards */}
// //             <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
// //               <div className="bg-gradient-to-br from-purple-500/20 to-purple-700/20 rounded-2xl p-6 border border-purple-500/30">
// //                 <p className="text-sm text-gray-400 mb-2">Candidate Score</p>
// //                 <p className="text-4xl font-bold text-purple-400">{data.candidateScore}%</p>
// //               </div>
// //               <div className="bg-gradient-to-br from-blue-500/20 to-blue-700/20 rounded-2xl p-6 border border-blue-500/30">
// //                 <p className="text-sm text-gray-400 mb-2">Skill Match</p>
// //                 <p className="text-4xl font-bold text-blue-400">{data.skillMatch}%</p>
// //               </div>
// //               <div className="bg-gradient-to-br from-green-500/20 to-green-700/20 rounded-2xl p-6 border border-green-500/30">
// //                 <p className="text-sm text-gray-400 mb-2">Authenticity</p>
// //                 <p className="text-4xl font-bold text-green-400">{data.authenticity}%</p>
// //               </div>
// //               <div className="bg-gradient-to-br from-orange-500/20 to-orange-700/20 rounded-2xl p-6 border border-orange-500/30">
// //                 <p className="text-sm text-gray-400 mb-2">Activity Consistency</p>
// //                 <p className="text-4xl font-bold text-orange-400">{data.activityConsistency}%</p>
// //               </div>
// //             </div>

// //             {/* Main Grid */}
// //             <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
// //               {/* Skills Breakdown */}
// //               <div className="col-span-1 md:col-span-2 bg-gray-800/50 rounded-3xl p-8 border border-gray-700">
// //                 <h3 className="text-2xl font-bold mb-6">Skills Breakdown</h3>
// //                 <div className="space-y-6">
// //                   {data.skillsBreakdown.map((skill, index) => (
// //                     <div key={index}>
// //                       <div className="flex justify-between mb-2">
// //                         <span className="text-white font-medium">{skill.name}</span>
// //                         <span className="text-purple-400 font-bold">{skill.value}%</span>
// //                       </div>
// //                       <div className="h-3 bg-gray-700 rounded-full overflow-hidden">
// //                         <div
// //                           className="h-full bg-gradient-to-r from-purple-500 to-pink-500 rounded-full transition-all duration-1000"
// //                           style={{ width: `${skill.value}%` }}
// //                         ></div>
// //                       </div>
// //                     </div>
// //                   ))}
// //                 </div>
// //               </div>

// //               {/* Recommendation */}
// //               <div className="bg-gray-800/50 rounded-3xl p-6 border border-gray-700">
// //                 <h3 className="text-xl font-bold mb-4">Recommendation</h3>
// //                 <div className={`text-center p-6 rounded-2xl ${
// //                   data.recommendation === "Strong Hire" 
// //                     ? "bg-green-500/20 border border-green-500/50" 
// //                     : data.recommendation === "Weak Hire"
// //                     ? "bg-yellow-500/20 border border-yellow-500/50"
// //                     : "bg-red-500/20 border border-red-500/50"
// //                 }`}>
// //                   <p className={`text-3xl font-bold ${
// //                     data.recommendation === "Strong Hire" 
// //                       ? "text-green-400" 
// //                       : data.recommendation === "Weak Hire"
// //                       ? "text-yellow-400"
// //                       : "text-red-400"
// //                   }`}>
// //                     {data.recommendation}
// //                   </p>
// //                 </div>
// //               </div>

// //               {/* GitHub Activity */}
// //               <div className="col-span-1 md:col-span-2 bg-gradient-to-br from-pink-200 to-purple-200 rounded-3xl p-8 relative overflow-hidden">
// //                 <div className="text-black">
// //                   <p className="text-sm mb-2">GitHub Activity (Last 6 Months)</p>
// //                   <h3 className="text-3xl font-bold mb-6">Commit History</h3>
                  
// //                   <div className="mt-8 flex items-end justify-between h-32">
// //                     {data.githubActivity.map((item, index) => (
// //                       <div key={index} className="flex flex-col items-center gap-1">
// //                         <div className="flex flex-col gap-1">
// //                           {Array.from({ length: Math.floor(item.commits / 10) }).map((_, i) => (
// //                             <div
// //                               key={i}
// //                               className={`w-3 h-3 rounded-full ${
// //                                 i >= Math.floor(item.commits / 10) - 3 ? "bg-black" : "bg-black/20"
// //                               }`}
// //                             ></div>
// //                           ))}
// //                         </div>
// //                         <span className="text-xs mt-2 text-black/60">{item.month}</span>
// //                       </div>
// //                     ))}
// //                   </div>
// //                 </div>
// //               </div>

// //               {/* Platforms */}
// //               <div className="bg-gray-800/50 rounded-3xl p-6 border border-gray-700">
// //                 <p className="text-sm text-gray-400 mb-6">Platforms</p>
                
// //                 <div className="space-y-4">
// //                   {data.platforms.map((platform, index) => (
// //                     <div key={index} className="flex items-center justify-between">
// //                       <span className="text-white">{platform.name}</span>
// //                       <span className="text-green-400 font-medium">{platform.value}</span>
// //                     </div>
// //                   ))}
// //                 </div>
// //               </div>

// //               {/* Interview Questions */}
// //               <div className="col-span-1 md:col-span-3 bg-gray-800/50 rounded-3xl p-8 border border-gray-700">
// //                 <h3 className="text-2xl font-bold mb-6">Suggested Interview Questions</h3>
// //                 <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
// //                   {data.interviewQuestions.map((question, index) => (
// //                     <div
// //                       key={index}
// //                       className="p-4 bg-gray-700/50 rounded-xl border border-gray-600 hover:border-purple-500 transition-all"
// //                     >
// //                       <div className="flex items-start gap-3">
// //                         <span className="flex-shrink-0 w-8 h-8 rounded-full bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center text-sm font-bold">
// //                           {index + 1}
// //                         </span>
// //                         <p className="text-sm text-gray-300 pt-1">{question}</p>
// //                       </div>
// //                     </div>
// //                   ))}
// //                 </div>
// //               </div>
// //             </div>
// //           </>
// //         )}

// //         {!loading && !data && (
// //           <div className="text-center py-20">
// //             <div className="w-20 h-20 bg-purple-500/20 rounded-full flex items-center justify-center mx-auto mb-4">
// //               <svg className="w-10 h-10 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
// //                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
// //               </svg>
// //             </div>
// //             <p className="text-gray-400 text-lg">Enter candidate details above to start analysis</p>
// //             <p className="text-gray-500 text-sm mt-2">Upload resume, provide GitHub username, LinkedIn URL, and role</p>
// //           </div>
// //         )}
// //       </div>
// //     </div>
// //   );
// // }

// // export default App;

// import React, { useState, useEffect, useRef } from "react";
// import axios from "axios";

// /* ─────────────────────────────────────────────
//    NEXUS RECRUIT — Solo Leveling Recruitment UI
//    Drop-in replacement for App.js
//    Requires: Tailwind CSS (CDN or config)
// ───────────────────────────────────────────────── */

// // ── Inline global styles injected once ──────────────────────────
// const GLOBAL_CSS = `
//   @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');

//   :root {
//     --purple: #8B5CF6;
//     --pink: #EC4899;
//     --cyan: #06B6D4;
//     --gold: #F59E0B;
//     --dark: #020617;
//     --panel: rgba(15,15,35,0.85);
//     --border: rgba(139,92,246,0.35);
//   }

//   * { box-sizing: border-box; }

//   body {
//     background: var(--dark);
//     font-family: 'Rajdhani', sans-serif;
//     overflow-x: hidden;
//   }

//   .orbitron { font-family: 'Orbitron', monospace; }
//   .mono { font-family: 'Share Tech Mono', monospace; }

//   /* Animated background grid */
//   .grid-bg {
//     background-image:
//       linear-gradient(rgba(139,92,246,0.07) 1px, transparent 1px),
//       linear-gradient(90deg, rgba(139,92,246,0.07) 1px, transparent 1px);
//     background-size: 40px 40px;
//     animation: gridScroll 20s linear infinite;
//   }
//   @keyframes gridScroll {
//     0%   { background-position: 0 0; }
//     100% { background-position: 40px 40px; }
//   }

//   /* Neon glow utilities */
//   .glow-purple { text-shadow: 0 0 20px #8B5CF6, 0 0 40px #8B5CF6; }
//   .glow-pink   { text-shadow: 0 0 20px #EC4899, 0 0 40px #EC4899; }
//   .glow-cyan   { text-shadow: 0 0 20px #06B6D4; }
//   .glow-gold   { text-shadow: 0 0 20px #F59E0B; }
//   .box-glow-purple { box-shadow: 0 0 20px rgba(139,92,246,0.4), inset 0 0 20px rgba(139,92,246,0.05); }
//   .box-glow-pink   { box-shadow: 0 0 20px rgba(236,72,153,0.4), inset 0 0 20px rgba(236,72,153,0.05); }
//   .box-glow-cyan   { box-shadow: 0 0 20px rgba(6,182,212,0.4), inset 0 0 20px rgba(6,182,212,0.05); }
//   .box-glow-gold   { box-shadow: 0 0 20px rgba(245,158,11,0.4), inset 0 0 20px rgba(245,158,11,0.05); }

//   /* Panel glass */
//   .panel {
//     background: var(--panel);
//     border: 1px solid var(--border);
//     backdrop-filter: blur(16px);
//   }

//   /* Skill bar animation */
//   @keyframes fillBar {
//     from { width: 0%; }
//     to   { width: var(--target-width); }
//   }
//   .skill-bar-fill {
//     animation: fillBar 1.4s cubic-bezier(0.16,1,0.3,1) forwards;
//   }

//   /* Pulse ring */
//   @keyframes pulseRing {
//     0%   { transform: scale(1);   opacity: 0.7; }
//     100% { transform: scale(1.6); opacity: 0; }
//   }
//   .pulse-ring::after {
//     content: '';
//     position: absolute;
//     inset: 0;
//     border-radius: 9999px;
//     border: 2px solid var(--purple);
//     animation: pulseRing 2s ease-out infinite;
//   }

//   /* Scan line sweep */
//   @keyframes scanSweep {
//     0%   { top: -4px; opacity: 1; }
//     100% { top: 100%; opacity: 0; }
//   }
//   .scan-line {
//     position: absolute;
//     left: 0; right: 0;
//     height: 3px;
//     background: linear-gradient(90deg, transparent, #8B5CF6, #EC4899, transparent);
//     box-shadow: 0 0 16px #8B5CF6;
//     animation: scanSweep 2.5s ease-in-out infinite;
//   }

//   /* XP bar shimmer */
//   @keyframes shimmer {
//     0%   { background-position: -200% center; }
//     100% { background-position: 200% center; }
//   }
//   .xp-bar {
//     background: linear-gradient(90deg, #8B5CF6, #EC4899, #06B6D4, #8B5CF6);
//     background-size: 200% auto;
//     animation: shimmer 3s linear infinite, fillBar 1.8s cubic-bezier(0.16,1,0.3,1) forwards;
//   }

//   /* Float in */
//   @keyframes floatIn {
//     from { opacity: 0; transform: translateY(24px); }
//     to   { opacity: 1; transform: translateY(0); }
//   }
//   .float-in { animation: floatIn 0.6s ease-out forwards; }
//   .delay-1  { animation-delay: 0.1s; opacity: 0; }
//   .delay-2  { animation-delay: 0.2s; opacity: 0; }
//   .delay-3  { animation-delay: 0.3s; opacity: 0; }
//   .delay-4  { animation-delay: 0.4s; opacity: 0; }
//   .delay-5  { animation-delay: 0.5s; opacity: 0; }
//   .delay-6  { animation-delay: 0.6s; opacity: 0; }

//   /* Counter anim */
//   @keyframes countUp {
//     from { opacity: 0; transform: scale(0.7); }
//     to   { opacity: 1; transform: scale(1); }
//   }
//   .count-up { animation: countUp 0.5s cubic-bezier(0.34,1.56,0.64,1) forwards; }

//   /* Hover card lift */
//   .lift { transition: transform 0.2s ease, box-shadow 0.2s ease; }
//   .lift:hover { transform: translateY(-4px); }

//   /* Button pulse on hover */
//   .btn-nexus {
//     position: relative;
//     overflow: hidden;
//     transition: all 0.3s ease;
//   }
//   .btn-nexus::before {
//     content: '';
//     position: absolute;
//     inset: 0;
//     background: linear-gradient(135deg, #8B5CF6, #EC4899);
//     opacity: 0;
//     transition: opacity 0.3s;
//   }
//   .btn-nexus:hover::before { opacity: 0.15; }

//   /* Input focus glow */
//   .nexus-input {
//     background: rgba(10,10,30,0.8);
//     border: 1px solid rgba(139,92,246,0.3);
//     color: #e2e8f0;
//     transition: border-color 0.3s, box-shadow 0.3s;
//     font-family: 'Rajdhani', sans-serif;
//     font-size: 1rem;
//   }
//   .nexus-input:focus {
//     outline: none;
//     border-color: #8B5CF6;
//     box-shadow: 0 0 0 2px rgba(139,92,246,0.2), 0 0 20px rgba(139,92,246,0.2);
//   }
//   .nexus-input::placeholder { color: rgba(148,163,184,0.4); }

//   /* Rank badge */
//   .rank-s { color: #F59E0B; text-shadow: 0 0 20px #F59E0B; }
//   .rank-a { color: #8B5CF6; text-shadow: 0 0 20px #8B5CF6; }
//   .rank-b { color: #06B6D4; text-shadow: 0 0 20px #06B6D4; }
//   .rank-c { color: #10B981; text-shadow: 0 0 10px #10B981; }
//   .rank-d { color: #94A3B8; }

//   /* Scrollbar */
//   ::-webkit-scrollbar { width: 4px; }
//   ::-webkit-scrollbar-track { background: #0a0a1a; }
//   ::-webkit-scrollbar-thumb { background: #8B5CF6; border-radius: 2px; }

//   /* Loading dots */
//   @keyframes dotBlink {
//     0%, 80%, 100% { opacity: 0; transform: scale(0.8); }
//     40%           { opacity: 1; transform: scale(1); }
//   }
//   .dot-1 { animation: dotBlink 1.2s infinite 0s; }
//   .dot-2 { animation: dotBlink 1.2s infinite 0.2s; }
//   .dot-3 { animation: dotBlink 1.2s infinite 0.4s; }

//   /* Commit bar anim */
//   @keyframes barRise {
//     from { height: 0; opacity: 0; }
//     to   { opacity: 1; }
//   }
//   .bar-rise { animation: barRise 0.8s cubic-bezier(0.34,1.56,0.64,1) forwards; }

//   /* Question card appear */
//   @keyframes slideUp {
//     from { opacity: 0; transform: translateY(30px) scale(0.97); }
//     to   { opacity: 1; transform: translateY(0) scale(1); }
//   }
//   .slide-up { animation: slideUp 0.5s ease-out forwards; }
// `;

// // ── Utility: inject styles once ──────────────────────────────────
// function useGlobalStyles() {
//   useEffect(() => {
//     if (document.getElementById("nexus-styles")) return;
//     const el = document.createElement("style");
//     el.id = "nexus-styles";
//     el.textContent = GLOBAL_CSS;
//     document.head.appendChild(el);
//   }, []);
// }

// // ── Floating particles background ────────────────────────────────
// function Particles() {
//   const particles = Array.from({ length: 30 }, (_, i) => i);
//   return (
//     <div className="fixed inset-0 pointer-events-none overflow-hidden">
//       {particles.map((i) => {
//         const x = Math.random() * 100;
//         const y = Math.random() * 100;
//         const size = Math.random() * 3 + 1;
//         const duration = Math.random() * 15 + 8;
//         const delay = Math.random() * 10;
//         const color = ["#8B5CF6", "#EC4899", "#06B6D4"][Math.floor(Math.random() * 3)];
//         return (
//           <div
//             key={i}
//             style={{
//               position: "absolute",
//               left: `${x}%`,
//               top: `${y}%`,
//               width: size,
//               height: size,
//               borderRadius: "50%",
//               backgroundColor: color,
//               opacity: 0.4,
//               boxShadow: `0 0 ${size * 3}px ${color}`,
//               animation: `float${i} ${duration}s ${delay}s ease-in-out infinite alternate`,
//             }}
//           />
//         );
//       })}
//       <style>{particles
//         .map(
//           (i) =>
//             `@keyframes float${i} { from { transform: translate(0,0); } to { transform: translate(${(Math.random() - 0.5) * 80}px, ${(Math.random() - 0.5) * 80}px); } }`
//         )
//         .join("")}</style>
//     </div>
//   );
// }

// // ── Hex stat card ─────────────────────────────────────────────────
// function StatCard({ label, value, color, icon, delay = "" }) {
//   const colors = {
//     purple: { border: "border-purple-500/40", text: "text-purple-400", glow: "box-glow-purple", bg: "from-purple-900/30 to-purple-800/10" },
//     pink:   { border: "border-pink-500/40",   text: "text-pink-400",   glow: "box-glow-pink",   bg: "from-pink-900/30 to-pink-800/10" },
//     cyan:   { border: "border-cyan-500/40",   text: "text-cyan-400",   glow: "box-glow-cyan",   bg: "from-cyan-900/30 to-cyan-800/10" },
//     gold:   { border: "border-yellow-500/40", text: "text-yellow-400", glow: "box-glow-gold",   bg: "from-yellow-900/30 to-yellow-800/10" },
//   };
//   const c = colors[color];
//   return (
//     <div className={`panel rounded-xl p-5 ${c.border} ${c.glow} bg-gradient-to-br ${c.bg} lift float-in ${delay} text-center`}>
//       <div className="text-2xl mb-1">{icon}</div>
//       <div className={`orbitron text-3xl font-bold ${c.text} count-up`}>{value}%</div>
//       <div className="text-slate-400 text-sm mt-1 tracking-widest uppercase">{label}</div>
//     </div>
//   );
// }

// // ── Skill bar row ─────────────────────────────────────────────────
// function SkillBar({ name, value, index }) {
//   const barRef = useRef(null);
//   useEffect(() => {
//     const timeout = setTimeout(() => {
//       if (barRef.current) barRef.current.style.setProperty("--target-width", `${value}%`);
//     }, 200 + index * 120);
//     return () => clearTimeout(timeout);
//   }, [value, index]);

//   const getColor = (v) => {
//     if (v >= 80) return "from-purple-500 to-pink-500";
//     if (v >= 60) return "from-cyan-500 to-purple-500";
//     if (v >= 40) return "from-blue-500 to-cyan-500";
//     return "from-slate-500 to-blue-500";
//   };

//   return (
//     <div className={`float-in delay-${Math.min(index + 1, 6)}`}>
//       <div className="flex justify-between items-center mb-1">
//         <span className="text-slate-200 font-semibold tracking-wide">{name}</span>
//         <span className="mono text-purple-400 text-sm">{value}%</span>
//       </div>
//       <div className="h-2 bg-slate-800 rounded-full overflow-hidden relative">
//         <div
//           ref={barRef}
//           className={`h-full bg-gradient-to-r ${getColor(value)} rounded-full skill-bar-fill`}
//           style={{ "--target-width": "0%", width: "0%" }}
//         />
//         {value >= 70 && (
//           <div className="absolute right-0 top-0 h-full w-1 bg-white/30 animate-pulse rounded-full" />
//         )}
//       </div>
//     </div>
//   );
// }

// // ── Commit bar chart ──────────────────────────────────────────────
// function CommitChart({ data }) {
//   const max = Math.max(...data.map((d) => d.commits), 1);
//   return (
//     <div className="flex items-end justify-between h-28 gap-2 mt-4">
//       {data.map((item, i) => {
//         const pct = Math.max((item.commits / max) * 100, 4);
//         const delay = i * 80;
//         return (
//           <div key={i} className="flex flex-col items-center gap-1 flex-1">
//             <span className="mono text-xs text-slate-400">{item.commits}</span>
//             <div className="w-full relative" style={{ height: "80px" }}>
//               <div
//                 className="absolute bottom-0 left-0 right-0 rounded-t bar-rise"
//                 style={{
//                   height: `${pct}%`,
//                   background: `linear-gradient(180deg, #8B5CF6, #EC4899)`,
//                   boxShadow: "0 0 10px rgba(139,92,246,0.5)",
//                   animationDelay: `${delay}ms`,
//                 }}
//               />
//             </div>
//             <span className="mono text-xs text-slate-500">{item.month}</span>
//           </div>
//         );
//       })}
//     </div>
//   );
// }

// // ── Rank badge ────────────────────────────────────────────────────
// function getRank(score) {
//   if (score >= 85) return { label: "S", cls: "rank-s", title: "S-CLASS HUNTER" };
//   if (score >= 70) return { label: "A", cls: "rank-a", title: "A-CLASS HUNTER" };
//   if (score >= 55) return { label: "B", cls: "rank-b", title: "B-CLASS HUNTER" };
//   if (score >= 40) return { label: "C", cls: "rank-c", title: "C-CLASS HUNTER" };
//   return { label: "D", cls: "rank-d", title: "D-CLASS RECRUIT" };
// }

// // ── Loading scanner ───────────────────────────────────────────────
// function ScanLoader() {
//   const [step, setStep] = useState(0);
//   const steps = [
//     { pct: 15, text: "Initializing Neural Scanner..." },
//     { pct: 38, text: "Parsing Resume Data..." },
//     { pct: 62, text: "Analyzing GitHub Activity..." },
//     { pct: 80, text: "Cross-referencing LinkedIn Profile..." },
//     { pct: 95, text: "Generating AI Insights..." },
//   ];
//   useEffect(() => {
//     const interval = setInterval(() => setStep((s) => Math.min(s + 1, steps.length - 1)), 2200);
//     return () => clearInterval(interval);
//   }, []);
//   const current = steps[step];
//   return (
//     <div className="flex flex-col items-center justify-center py-24">
//       <div className="relative w-40 h-40 mb-10">
//         <div className="absolute inset-0 rounded-full border-2 border-purple-500/30 animate-pulse" />
//         <div
//           className="absolute inset-2 rounded-full border-2 border-transparent"
//           style={{
//             borderTopColor: "#8B5CF6",
//             borderRightColor: "#EC4899",
//             animation: "spin 1s linear infinite",
//           }}
//         />
//         <div
//           className="absolute inset-6 rounded-full border-2 border-transparent"
//           style={{
//             borderBottomColor: "#06B6D4",
//             animation: "spin 1.5s linear infinite reverse",
//           }}
//         />
//         <style>{`@keyframes spin { to { transform: rotate(360deg); } }`}</style>
//         <div className="absolute inset-0 flex items-center justify-center">
//           <span className="orbitron text-purple-400 text-2xl font-bold">{current.pct}%</span>
//         </div>
//         <div className="scan-line" style={{ position: "absolute", left: 0, right: 0, top: 0 }} />
//       </div>
//       <div className="orbitron text-purple-300 text-lg font-bold mb-2 glow-purple">{current.text}</div>
//       <div className="flex gap-2 mt-3">
//         <div className="w-2 h-2 rounded-full bg-purple-500 dot-1" />
//         <div className="w-2 h-2 rounded-full bg-pink-500 dot-2" />
//         <div className="w-2 h-2 rounded-full bg-cyan-500 dot-3" />
//       </div>
//       <div className="mt-8 w-80 h-1 bg-slate-800 rounded-full overflow-hidden">
//         <div
//           className="h-full bg-gradient-to-r from-purple-500 via-pink-500 to-cyan-500 rounded-full transition-all duration-700"
//           style={{ width: `${current.pct}%` }}
//         />
//       </div>
//     </div>
//   );
// }

// // ── Main App ──────────────────────────────────────────────────────
// export default function App() {
//   useGlobalStyles();

//   const [data, setData] = useState(null);
//   const [loading, setLoading] = useState(false);
//   const [githubUsername, setGithubUsername] = useState("");
//   const [linkedinUrl, setLinkedinUrl] = useState("");
//   const [role, setRole] = useState("");
//   const [resume, setResume] = useState(null);
//   const [error, setError] = useState("");
//   const [dragging, setDragging] = useState(false);

//   const fetchAnalysis = async () => {
//     if (!githubUsername || !linkedinUrl || !role || !resume) {
//       setError("All fields required — provide GitHub, LinkedIn, Role & Resume.");
//       return;
//     }
//     try {
//       setLoading(true);
//       setError("");
//       setData(null);
//       const formData = new FormData();
//       formData.append("resume", resume);
//       const response = await axios.post(
//         `http://127.0.0.1:8000/full-analysis?github_username=${encodeURIComponent(githubUsername)}&linkedin_url=${encodeURIComponent(linkedinUrl)}&role=${encodeURIComponent(role)}`,
//         formData,
//         { headers: { "Content-Type": "multipart/form-data" } }
//       );
//       setData(response.data);
//     } catch (err) {
//       setError(err.response?.data?.detail || "Scan failed — check inputs and try again.");
//     } finally {
//       setLoading(false);
//     }
//   };

//   const handleDrop = (e) => {
//     e.preventDefault();
//     setDragging(false);
//     const file = e.dataTransfer.files[0];
//     if (file?.type === "application/pdf") { setResume(file); setError(""); }
//     else setError("Only PDF files accepted.");
//   };

//   const rank = data ? getRank(data.candidateScore) : null;

//   return (
//     <div className="min-h-screen grid-bg text-white relative" style={{ background: "#020617" }}>
//       <Particles />

//       {/* ── HEADER ─────────────────────────────────────────── */}
//       <header className="relative z-10 flex items-center justify-between px-8 py-5 border-b border-purple-500/20">
//         <div className="flex items-center gap-4">
//           <div className="relative w-10 h-10 pulse-ring">
//             <div className="w-10 h-10 rounded-full bg-gradient-to-br from-purple-600 to-pink-600 flex items-center justify-center">
//               <span className="orbitron font-black text-sm">NX</span>
//             </div>
//           </div>
//           <div>
//             <div className="orbitron font-black text-xl glow-purple tracking-widest">NEXUS RECRUIT</div>
//             <div className="mono text-xs text-purple-400 tracking-widest">HUNTER INTELLIGENCE SYSTEM v2.0</div>
//           </div>
//         </div>
//         <nav className="flex gap-6 text-sm text-slate-400 tracking-widest uppercase">
//           <button className="hover:text-purple-400 transition-colors">Overview</button>
//           <button className="hover:text-purple-400 transition-colors">Archive</button>
//           <button className="hover:text-purple-400 transition-colors">Settings</button>
//         </nav>
//       </header>

//       <main className="relative z-10 max-w-7xl mx-auto px-6 py-10">

//         {/* ── INPUT GATE ─────────────────────────────────────── */}
//         <div className="panel rounded-2xl p-8 mb-10 box-glow-purple">
//           <div className="flex items-center gap-4 mb-8">
//             <div className="w-1 h-10 bg-gradient-to-b from-purple-500 to-pink-500 rounded" />
//             <div>
//               <h1 className="orbitron text-3xl font-black glow-purple">CANDIDATE SCANNER</h1>
//               <p className="mono text-slate-400 text-sm mt-1">HUNTER'S GATE — INITIATE PROFILE SCAN</p>
//             </div>
//           </div>

//           {error && (
//             <div className="mb-6 p-4 rounded-lg border border-red-500/50 bg-red-900/20 mono text-red-400 text-sm">
//               ⚠ {error}
//             </div>
//           )}

//           <div className="grid grid-cols-1 md:grid-cols-2 gap-5 mb-6">
//             {/* GitHub */}
//             <div>
//               <label className="mono text-xs text-purple-400 tracking-widest uppercase mb-2 block">◈ GitHub Username</label>
//               <input
//                 type="text"
//                 value={githubUsername}
//                 onChange={(e) => setGithubUsername(e.target.value)}
//                 placeholder="octocat"
//                 className="nexus-input w-full rounded-lg px-4 py-3"
//               />
//             </div>

//             {/* LinkedIn */}
//             <div>
//               <label className="mono text-xs text-cyan-400 tracking-widest uppercase mb-2 block">◈ LinkedIn URL</label>
//               <input
//                 type="text"
//                 value={linkedinUrl}
//                 onChange={(e) => setLinkedinUrl(e.target.value)}
//                 placeholder="linkedin.com/in/username"
//                 className="nexus-input w-full rounded-lg px-4 py-3"
//               />
//             </div>

//             {/* Role */}
//             <div>
//               <label className="mono text-xs text-pink-400 tracking-widest uppercase mb-2 block">◈ Target Role</label>
//               <input
//                 type="text"
//                 value={role}
//                 onChange={(e) => setRole(e.target.value)}
//                 placeholder="Senior Backend Engineer"
//                 className="nexus-input w-full rounded-lg px-4 py-3"
//               />
//             </div>

//             {/* Resume drop zone */}
//             <div>
//               <label className="mono text-xs text-yellow-400 tracking-widest uppercase mb-2 block">◈ Resume Upload (PDF)</label>
//               <div
//                 onDragOver={(e) => { e.preventDefault(); setDragging(true); }}
//                 onDragLeave={() => setDragging(false)}
//                 onDrop={handleDrop}
//                 onClick={() => document.getElementById("file-input").click()}
//                 className={`nexus-input rounded-lg px-4 py-4 cursor-pointer text-center transition-all ${
//                   dragging ? "border-yellow-400 bg-yellow-900/20" : ""
//                 } ${resume ? "border-green-500/50 bg-green-900/10" : ""}`}
//               >
//                 {resume ? (
//                   <span className="text-green-400 mono text-sm">✓ {resume.name}</span>
//                 ) : (
//                   <span className="text-slate-500 mono text-sm">
//                     {dragging ? "Drop it here..." : "Drag & drop or click to upload"}
//                   </span>
//                 )}
//               </div>
//               <input
//                 id="file-input"
//                 type="file"
//                 accept=".pdf"
//                 className="hidden"
//                 onChange={(e) => { if (e.target.files?.[0]) { setResume(e.target.files[0]); setError(""); } }}
//               />
//             </div>
//           </div>

//           <button
//             onClick={fetchAnalysis}
//             disabled={loading}
//             className="btn-nexus relative px-10 py-4 rounded-xl font-bold tracking-widest uppercase orbitron text-sm
//               bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500
//               disabled:opacity-40 disabled:cursor-not-allowed transition-all
//               box-glow-purple"
//           >
//             {loading ? (
//               <span className="flex items-center gap-3">
//                 <span className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full inline-block" style={{ animation: "spin 0.8s linear infinite" }} />
//                 SCANNING...
//               </span>
//             ) : (
//               "⚡ INITIATE SCAN"
//             )}
//           </button>
//         </div>

//         {/* ── LOADING ─────────────────────────────────────────── */}
//         {loading && <ScanLoader />}

//         {/* ── RESULTS DASHBOARD ──────────────────────────────── */}
//         {!loading && data && (
//           <>
//             {/* Rank banner */}
//             <div className="panel rounded-2xl p-6 mb-8 flex items-center justify-between float-in box-glow-purple">
//               <div className="flex items-center gap-6">
//                 <div className="orbitron text-7xl font-black" style={{ fontFamily: "'Orbitron', monospace" }}>
//                   <span className={rank.cls}>{rank.label}</span>
//                 </div>
//                 <div>
//                   <div className={`orbitron text-2xl font-black ${rank.cls}`}>{rank.title}</div>
//                   <div className="mono text-slate-400 text-sm mt-1 tracking-widest">
//                     TARGET ROLE: <span className="text-purple-300">{role.toUpperCase()}</span>
//                   </div>
//                 </div>
//               </div>
//               <div className={`px-6 py-3 rounded-xl border font-bold orbitron tracking-widest text-sm ${
//                 data.recommendation === "Strong Hire"
//                   ? "border-green-500/50 bg-green-900/20 text-green-400"
//                   : data.recommendation === "Weak Hire"
//                   ? "border-yellow-500/50 bg-yellow-900/20 text-yellow-400"
//                   : "border-red-500/50 bg-red-900/20 text-red-400"
//               }`}>
//                 {data.recommendation === "Strong Hire" ? "✅" : data.recommendation === "Weak Hire" ? "⚠️" : "❌"}{" "}
//                 {data.recommendation.toUpperCase()}
//               </div>
//             </div>

//             {/* Score cards */}
//             <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
//               <StatCard label="Candidate Score"    value={data.candidateScore}       color="purple" icon="⚔️"  delay="delay-1" />
//               <StatCard label="Skill Match"        value={data.skillMatch}           color="cyan"   icon="🎯"  delay="delay-2" />
//               <StatCard label="Authenticity"       value={data.authenticity}         color="pink"   icon="💎"  delay="delay-3" />
//               <StatCard label="Activity Streak"    value={data.activityConsistency}  color="gold"   icon="⚡"  delay="delay-4" />
//             </div>

//             {/* XP bar */}
//             <div className="panel rounded-xl p-5 mb-8 float-in delay-5">
//               <div className="flex justify-between items-center mb-3">
//                 <span className="orbitron text-sm tracking-widest text-slate-400">OVERALL XP PROGRESS</span>
//                 <span className="mono text-purple-400">{data.candidateScore} / 100 XP</span>
//               </div>
//               <div className="h-3 bg-slate-800 rounded-full overflow-hidden">
//                 <div
//                   className="h-full xp-bar rounded-full"
//                   style={{ "--target-width": `${data.candidateScore}%`, width: "0%" }}
//                 />
//               </div>
//             </div>

//             {/* Main grid */}
//             <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
//               {/* Skills breakdown */}
//               <div className="md:col-span-2 panel rounded-2xl p-7 float-in delay-1">
//                 <div className="flex items-center gap-3 mb-7">
//                   <span className="text-xl">🧠</span>
//                   <h3 className="orbitron font-bold text-lg tracking-widest glow-purple">SKILL POWER LEVELS</h3>
//                 </div>
//                 <div className="space-y-5">
//                   {data.skillsBreakdown.map((skill, i) => (
//                     <SkillBar key={i} name={skill.name} value={skill.value} index={i} />
//                   ))}
//                 </div>
//               </div>

//               {/* Platforms */}
//               <div className="panel rounded-2xl p-7 float-in delay-2">
//                 <div className="flex items-center gap-3 mb-7">
//                   <span className="text-xl">🌐</span>
//                   <h3 className="orbitron font-bold text-lg tracking-widest glow-cyan">PLATFORM DATA</h3>
//                 </div>
//                 <div className="space-y-5">
//                   {data.platforms.map((p, i) => (
//                     <div key={i} className="flex items-center justify-between p-4 rounded-xl bg-slate-800/50 border border-slate-700/50">
//                       <span className="text-slate-300 font-semibold">{p.name}</span>
//                       <span className="mono text-cyan-400 text-sm">{p.value}</span>
//                     </div>
//                   ))}
//                   {/* Decorative stats */}
//                   <div className="mt-4 p-4 rounded-xl bg-gradient-to-br from-purple-900/30 to-pink-900/20 border border-purple-500/20">
//                     <div className="mono text-xs text-slate-400 mb-1 tracking-widest">ANALYSIS COMPLETE</div>
//                     <div className="orbitron text-purple-400 font-bold">Multi-Source Verified</div>
//                   </div>
//                 </div>
//               </div>
//             </div>

//             {/* Commit chart */}
//             <div className="panel rounded-2xl p-7 mb-8 float-in delay-3">
//               <div className="flex items-center justify-between mb-2">
//                 <div className="flex items-center gap-3">
//                   <span className="text-xl">💻</span>
//                   <h3 className="orbitron font-bold text-lg tracking-widest glow-pink">COMMIT BATTLE HISTORY</h3>
//                 </div>
//                 <span className="mono text-xs text-slate-500 tracking-widest">LAST 6 MONTHS</span>
//               </div>
//               <CommitChart data={data.githubActivity} />
//             </div>

//             {/* Interview questions */}
//             <div className="panel rounded-2xl p-7 float-in delay-4">
//               <div className="flex items-center gap-3 mb-7">
//                 <span className="text-xl">⚔️</span>
//                 <h3 className="orbitron font-bold text-xl tracking-widest glow-gold">BATTLE ARENA — INTERVIEW CHALLENGES</h3>
//               </div>
//               <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
//                 {data.interviewQuestions.map((q, i) => {
//                   const levels = ["LEVEL 1: STARTER", "LEVEL 2: ADVANCED", "LEVEL 3: EXPERT", "LEVEL 4: BOSS", "LEVEL 5: RAID"];
//                   const colors = [
//                     "border-green-500/40 bg-green-900/10",
//                     "border-cyan-500/40 bg-cyan-900/10",
//                     "border-purple-500/40 bg-purple-900/10",
//                     "border-pink-500/40 bg-pink-900/10",
//                     "border-yellow-500/40 bg-yellow-900/10",
//                   ];
//                   const textColors = ["text-green-400", "text-cyan-400", "text-purple-400", "text-pink-400", "text-yellow-400"];
//                   return (
//                     <div
//                       key={i}
//                       className={`p-5 rounded-xl border ${colors[i % 5]} lift slide-up`}
//                       style={{ animationDelay: `${i * 100}ms`, opacity: 0 }}
//                     >
//                       <div className={`orbitron text-xs font-bold mb-3 tracking-widest ${textColors[i % 5]}`}>
//                         {levels[i % 5]}
//                       </div>
//                       <p className="text-slate-200 text-sm leading-relaxed">{q}</p>
//                     </div>
//                   );
//                 })}
//               </div>
//             </div>
//           </>
//         )}

//         {/* ── EMPTY STATE ─────────────────────────────────────── */}
//         {!loading && !data && (
//           <div className="text-center py-28 float-in">
//             <div className="relative inline-block mb-8">
//               <div className="w-28 h-28 rounded-full bg-gradient-to-br from-purple-900/60 to-pink-900/40 border border-purple-500/30 flex items-center justify-center mx-auto">
//                 <span className="text-5xl">🎯</span>
//               </div>
//               <div className="absolute inset-0 rounded-full border border-purple-500/20 animate-ping" />
//             </div>
//             <h2 className="orbitron text-3xl font-black glow-purple mb-3">HUNTER'S GATE AWAITS</h2>
//             <p className="mono text-slate-400 text-sm tracking-widest">ENTER CANDIDATE DATA TO INITIATE SCAN SEQUENCE</p>
//             <div className="flex justify-center gap-8 mt-10 text-xs mono text-slate-600 tracking-widest">
//               <span>◈ GITHUB</span>
//               <span>◈ LINKEDIN</span>
//               <span>◈ RESUME</span>
//               <span>◈ ROLE</span>
//             </div>
//           </div>
//         )}
//       </main>

//       {/* Footer */}
//       <footer className="relative z-10 text-center py-6 border-t border-purple-500/10 mono text-xs text-slate-600 tracking-widest">
//         NEXUS RECRUIT v2.0 — HUNTER INTELLIGENCE SYSTEM — ALL CANDIDATE DATA ENCRYPTED
//       </footer>
//     </div>
//   );
// }

import React, { useState, useEffect, useRef } from "react";
import axios from "axios";

/* ─────────────────────────────────────────────
   NEXUS RECRUIT — Solo Leveling Recruitment UI
   Drop-in replacement for App.js
   Requires: Tailwind CSS (CDN or config)
───────────────────────────────────────────────── */

// ── Inline global styles injected once ──────────────────────────
const GLOBAL_CSS = `
  @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');

  :root {
    --purple: #8B5CF6;
    --pink: #EC4899;
    --cyan: #06B6D4;
    --gold: #F59E0B;
    --dark: #020617;
    --panel: rgba(15,15,35,0.85);
    --border: rgba(139,92,246,0.35);
  }

  * { box-sizing: border-box; }

  body {
    background: var(--dark);
    font-family: 'Rajdhani', sans-serif;
    overflow-x: hidden;
  }

  .orbitron { font-family: 'Orbitron', monospace; }
  .mono { font-family: 'Share Tech Mono', monospace; }

  /* Animated background grid */
  .grid-bg {
    background-image:
      linear-gradient(rgba(139,92,246,0.07) 1px, transparent 1px),
      linear-gradient(90deg, rgba(139,92,246,0.07) 1px, transparent 1px);
    background-size: 40px 40px;
    animation: gridScroll 20s linear infinite;
  }
  @keyframes gridScroll {
    0%   { background-position: 0 0; }
    100% { background-position: 40px 40px; }
  }

  /* Neon glow utilities */
  .glow-purple { text-shadow: 0 0 20px #8B5CF6, 0 0 40px #8B5CF6; }
  .glow-pink   { text-shadow: 0 0 20px #EC4899, 0 0 40px #EC4899; }
  .glow-cyan   { text-shadow: 0 0 20px #06B6D4; }
  .glow-gold   { text-shadow: 0 0 20px #F59E0B; }
  .box-glow-purple { box-shadow: 0 0 20px rgba(139,92,246,0.4), inset 0 0 20px rgba(139,92,246,0.05); }
  .box-glow-pink   { box-shadow: 0 0 20px rgba(236,72,153,0.4), inset 0 0 20px rgba(236,72,153,0.05); }
  .box-glow-cyan   { box-shadow: 0 0 20px rgba(6,182,212,0.4), inset 0 0 20px rgba(6,182,212,0.05); }
  .box-glow-gold   { box-shadow: 0 0 20px rgba(245,158,11,0.4), inset 0 0 20px rgba(245,158,11,0.05); }

  /* Panel glass */
  .panel {
    background: var(--panel);
    border: 1px solid var(--border);
    backdrop-filter: blur(16px);
  }

  /* Skill bar animation */
  @keyframes fillBar {
    from { width: 0%; }
    to   { width: var(--target-width); }
  }
  .skill-bar-fill {
    animation: fillBar 1.4s cubic-bezier(0.16,1,0.3,1) forwards;
  }

  /* Pulse ring */
  @keyframes pulseRing {
    0%   { transform: scale(1);   opacity: 0.7; }
    100% { transform: scale(1.6); opacity: 0; }
  }
  .pulse-ring::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 9999px;
    border: 2px solid var(--purple);
    animation: pulseRing 2s ease-out infinite;
  }

  /* Scan line sweep */
  @keyframes scanSweep {
    0%   { top: -4px; opacity: 1; }
    100% { top: 100%; opacity: 0; }
  }
  .scan-line {
    position: absolute;
    left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, transparent, #8B5CF6, #EC4899, transparent);
    box-shadow: 0 0 16px #8B5CF6;
    animation: scanSweep 2.5s ease-in-out infinite;
  }

  /* XP bar shimmer */
  @keyframes shimmer {
    0%   { background-position: -200% center; }
    100% { background-position: 200% center; }
  }
  .xp-bar {
    background: linear-gradient(90deg, #8B5CF6, #EC4899, #06B6D4, #8B5CF6);
    background-size: 200% auto;
    animation: shimmer 3s linear infinite, fillBar 1.8s cubic-bezier(0.16,1,0.3,1) forwards;
  }

  /* Float in */
  @keyframes floatIn {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  .float-in { animation: floatIn 0.6s ease-out forwards; }
  .delay-1  { animation-delay: 0.1s; opacity: 0; }
  .delay-2  { animation-delay: 0.2s; opacity: 0; }
  .delay-3  { animation-delay: 0.3s; opacity: 0; }
  .delay-4  { animation-delay: 0.4s; opacity: 0; }
  .delay-5  { animation-delay: 0.5s; opacity: 0; }
  .delay-6  { animation-delay: 0.6s; opacity: 0; }

  /* Counter anim */
  @keyframes countUp {
    from { opacity: 0; transform: scale(0.7); }
    to   { opacity: 1; transform: scale(1); }
  }
  .count-up { animation: countUp 0.5s cubic-bezier(0.34,1.56,0.64,1) forwards; }

  /* Hover card lift */
  .lift { transition: transform 0.2s ease, box-shadow 0.2s ease; }
  .lift:hover { transform: translateY(-4px); }

  /* Button pulse on hover */
  .btn-nexus {
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
  }
  .btn-nexus::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, #8B5CF6, #EC4899);
    opacity: 0;
    transition: opacity 0.3s;
  }
  .btn-nexus:hover::before { opacity: 0.15; }

  /* Input focus glow */
  .nexus-input {
    background: rgba(10,10,30,0.8);
    border: 1px solid rgba(139,92,246,0.3);
    color: #e2e8f0;
    transition: border-color 0.3s, box-shadow 0.3s;
    font-family: 'Rajdhani', sans-serif;
    font-size: 1rem;
  }
  .nexus-input:focus {
    outline: none;
    border-color: #8B5CF6;
    box-shadow: 0 0 0 2px rgba(139,92,246,0.2), 0 0 20px rgba(139,92,246,0.2);
  }
  .nexus-input::placeholder { color: rgba(148,163,184,0.4); }

  /* Rank badge */
  .rank-s { color: #F59E0B; text-shadow: 0 0 20px #F59E0B; }
  .rank-a { color: #8B5CF6; text-shadow: 0 0 20px #8B5CF6; }
  .rank-b { color: #06B6D4; text-shadow: 0 0 20px #06B6D4; }
  .rank-c { color: #10B981; text-shadow: 0 0 10px #10B981; }
  .rank-d { color: #94A3B8; }

  /* Scrollbar */
  ::-webkit-scrollbar { width: 4px; }
  ::-webkit-scrollbar-track { background: #0a0a1a; }
  ::-webkit-scrollbar-thumb { background: #8B5CF6; border-radius: 2px; }

  /* Loading dots */
  @keyframes dotBlink {
    0%, 80%, 100% { opacity: 0; transform: scale(0.8); }
    40%           { opacity: 1; transform: scale(1); }
  }
  .dot-1 { animation: dotBlink 1.2s infinite 0s; }
  .dot-2 { animation: dotBlink 1.2s infinite 0.2s; }
  .dot-3 { animation: dotBlink 1.2s infinite 0.4s; }

  /* Commit bar anim */
  @keyframes barRise {
    from { height: 0; opacity: 0; }
    to   { opacity: 1; }
  }
  .bar-rise { animation: barRise 0.8s cubic-bezier(0.34,1.56,0.64,1) forwards; }

  /* Question card appear */
  @keyframes slideUp {
    from { opacity: 0; transform: translateY(30px) scale(0.97); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
  }
  .slide-up { animation: slideUp 0.5s ease-out forwards; }
`;

// ── Utility: inject styles once ──────────────────────────────────
function useGlobalStyles() {
  useEffect(() => {
    if (document.getElementById("nexus-styles")) return;
    const el = document.createElement("style");
    el.id = "nexus-styles";
    el.textContent = GLOBAL_CSS;
    document.head.appendChild(el);
  }, []);
}

// ── Floating particles background ────────────────────────────────
function Particles() {
  const particles = Array.from({ length: 30 }, (_, i) => i);
  return (
    <div className="fixed inset-0 pointer-events-none overflow-hidden">
      {particles.map((i) => {
        const x = Math.random() * 100;
        const y = Math.random() * 100;
        const size = Math.random() * 3 + 1;
        const duration = Math.random() * 15 + 8;
        const delay = Math.random() * 10;
        const color = ["#8B5CF6", "#EC4899", "#06B6D4"][Math.floor(Math.random() * 3)];
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: `${x}%`,
              top: `${y}%`,
              width: size,
              height: size,
              borderRadius: "50%",
              backgroundColor: color,
              opacity: 0.4,
              boxShadow: `0 0 ${size * 3}px ${color}`,
              animation: `float${i} ${duration}s ${delay}s ease-in-out infinite alternate`,
            }}
          />
        );
      })}
      <style>{particles
        .map(
          (i) =>
            `@keyframes float${i} { from { transform: translate(0,0); } to { transform: translate(${(Math.random() - 0.5) * 80}px, ${(Math.random() - 0.5) * 80}px); } }`
        )
        .join("")}</style>
    </div>
  );
}

// ── Hex stat card ─────────────────────────────────────────────────
function StatCard({ label, value, color, icon, delay = "" }) {
  const colors = {
    purple: { border: "border-purple-500/40", text: "text-purple-400", glow: "box-glow-purple", bg: "from-purple-900/30 to-purple-800/10" },
    pink:   { border: "border-pink-500/40",   text: "text-pink-400",   glow: "box-glow-pink",   bg: "from-pink-900/30 to-pink-800/10" },
    cyan:   { border: "border-cyan-500/40",   text: "text-cyan-400",   glow: "box-glow-cyan",   bg: "from-cyan-900/30 to-cyan-800/10" },
    gold:   { border: "border-yellow-500/40", text: "text-yellow-400", glow: "box-glow-gold",   bg: "from-yellow-900/30 to-yellow-800/10" },
  };
  const c = colors[color];
  return (
    <div className={`panel rounded-xl p-5 ${c.border} ${c.glow} bg-gradient-to-br ${c.bg} lift float-in ${delay} text-center`}>
      <div className="text-2xl mb-1">{icon}</div>
      <div className={`orbitron text-3xl font-bold ${c.text} count-up`}>{value}%</div>
      <div className="text-slate-400 text-sm mt-1 tracking-widest uppercase">{label}</div>
    </div>
  );
}

// ── Skill bar row ─────────────────────────────────────────────────
function SkillBar({ name, value, index }) {
  const barRef = useRef(null);
  useEffect(() => {
    const timeout = setTimeout(() => {
      if (barRef.current) barRef.current.style.setProperty("--target-width", `${value}%`);
    }, 200 + index * 120);
    return () => clearTimeout(timeout);
  }, [value, index]);

  const getColor = (v) => {
    if (v >= 80) return "from-purple-500 to-pink-500";
    if (v >= 60) return "from-cyan-500 to-purple-500";
    if (v >= 40) return "from-blue-500 to-cyan-500";
    return "from-slate-500 to-blue-500";
  };

  return (
    <div className={`float-in delay-${Math.min(index + 1, 6)}`}>
      <div className="flex justify-between items-center mb-1">
        <span className="text-slate-200 font-semibold tracking-wide">{name}</span>
        <span className="mono text-purple-400 text-sm">{value}%</span>
      </div>
      <div className="h-2 bg-slate-800 rounded-full overflow-hidden relative">
        <div
          ref={barRef}
          className={`h-full bg-gradient-to-r ${getColor(value)} rounded-full skill-bar-fill`}
          style={{ "--target-width": "0%", width: "0%" }}
        />
        {value >= 70 && (
          <div className="absolute right-0 top-0 h-full w-1 bg-white/30 animate-pulse rounded-full" />
        )}
      </div>
    </div>
  );
}

// ── Commit bar chart ──────────────────────────────────────────────
function CommitChart({ data }) {
  const max = Math.max(...data.map((d) => d.commits), 1);
  return (
    <div className="flex items-end justify-between h-28 gap-2 mt-4">
      {data.map((item, i) => {
        const pct = Math.max((item.commits / max) * 100, 4);
        const delay = i * 80;
        return (
          <div key={i} className="flex flex-col items-center gap-1 flex-1">
            <span className="mono text-xs text-slate-400">{item.commits}</span>
            <div className="w-full relative" style={{ height: "80px" }}>
              <div
                className="absolute bottom-0 left-0 right-0 rounded-t bar-rise"
                style={{
                  height: `${pct}%`,
                  background: `linear-gradient(180deg, #8B5CF6, #EC4899)`,
                  boxShadow: "0 0 10px rgba(139,92,246,0.5)",
                  animationDelay: `${delay}ms`,
                }}
              />
            </div>
            <span className="mono text-xs text-slate-500">{item.month}</span>
          </div>
        );
      })}
    </div>
  );
}

// ── Rank badge ────────────────────────────────────────────────────
function getRank(score) {
  if (score >= 85) return { label: "S", cls: "rank-s", title: "S-CLASS HUNTER" };
  if (score >= 70) return { label: "A", cls: "rank-a", title: "A-CLASS HUNTER" };
  if (score >= 55) return { label: "B", cls: "rank-b", title: "B-CLASS HUNTER" };
  if (score >= 40) return { label: "C", cls: "rank-c", title: "C-CLASS HUNTER" };
  return { label: "D", cls: "rank-d", title: "D-CLASS RECRUIT" };
}

// ── Loading scanner ───────────────────────────────────────────────
function ScanLoader() {
  const [step, setStep] = useState(0);
  const steps = [
    { pct: 15, text: "Initializing Neural Scanner..." },
    { pct: 38, text: "Parsing Resume Data..." },
    { pct: 62, text: "Analyzing GitHub Activity..." },
    { pct: 80, text: "Cross-referencing LinkedIn Profile..." },
    { pct: 95, text: "Generating AI Insights..." },
  ];
  useEffect(() => {
    const interval = setInterval(() => setStep((s) => Math.min(s + 1, steps.length - 1)), 2200);
    return () => clearInterval(interval);
  }, []);
  const current = steps[step];
  return (
    <div className="flex flex-col items-center justify-center py-24">
      <div className="relative w-40 h-40 mb-10">
        <div className="absolute inset-0 rounded-full border-2 border-purple-500/30 animate-pulse" />
        <div
          className="absolute inset-2 rounded-full border-2 border-transparent"
          style={{
            borderTopColor: "#8B5CF6",
            borderRightColor: "#EC4899",
            animation: "spin 1s linear infinite",
          }}
        />
        <div
          className="absolute inset-6 rounded-full border-2 border-transparent"
          style={{
            borderBottomColor: "#06B6D4",
            animation: "spin 1.5s linear infinite reverse",
          }}
        />
        <style>{`@keyframes spin { to { transform: rotate(360deg); } }`}</style>
        <div className="absolute inset-0 flex items-center justify-center">
          <span className="orbitron text-purple-400 text-2xl font-bold">{current.pct}%</span>
        </div>
        <div className="scan-line" style={{ position: "absolute", left: 0, right: 0, top: 0 }} />
      </div>
      <div className="orbitron text-purple-300 text-lg font-bold mb-2 glow-purple">{current.text}</div>
      <div className="flex gap-2 mt-3">
        <div className="w-2 h-2 rounded-full bg-purple-500 dot-1" />
        <div className="w-2 h-2 rounded-full bg-pink-500 dot-2" />
        <div className="w-2 h-2 rounded-full bg-cyan-500 dot-3" />
      </div>
      <div className="mt-8 w-80 h-1 bg-slate-800 rounded-full overflow-hidden">
        <div
          className="h-full bg-gradient-to-r from-purple-500 via-pink-500 to-cyan-500 rounded-full transition-all duration-700"
          style={{ width: `${current.pct}%` }}
        />
      </div>
    </div>
  );
}

// ── Main App ──────────────────────────────────────────────────────
export default function App() {
  useGlobalStyles();

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [githubUsername, setGithubUsername] = useState("");
  const [linkedinUrl, setLinkedinUrl] = useState("");
  const [role, setRole] = useState("");
  const [resume, setResume] = useState(null);
  const [error, setError] = useState("");
  const [dragging, setDragging] = useState(false);

  const fetchAnalysis = async () => {
    if (!githubUsername || !linkedinUrl || !role || !resume) {
      setError("All fields required — provide GitHub, LinkedIn, Role & Resume.");
      return;
    }
    try {
      setLoading(true);
      setError("");
      setData(null);
      const formData = new FormData();
      formData.append("resume", resume);
      formData.append("github_username", githubUsername);
      formData.append("linkedin_url", linkedinUrl);
      formData.append("role", role);
      const response = await axios.post(
        "http://127.0.0.1:8000/full-analysis",
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );
      setData(response.data);
    } catch (err) {
      const detail = err.response?.data?.detail;
      let msg = "Scan failed — check inputs and try again.";
      if (typeof detail === "string") {
        msg = detail;
      } else if (Array.isArray(detail)) {
        // FastAPI validation errors return [{loc, msg, type, input}, ...]
        msg = detail.map((e) => e.msg || JSON.stringify(e)).join(" | ");
      } else if (detail) {
        msg = JSON.stringify(detail);
      }
      setError(msg);
    } finally {
      setLoading(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setDragging(false);
    const file = e.dataTransfer.files[0];
    if (file?.type === "application/pdf") { setResume(file); setError(""); }
    else setError("Only PDF files accepted.");
  };

  const rank = data ? getRank(data.candidateScore) : null;

  return (
    <div className="min-h-screen grid-bg text-white relative" style={{ background: "#020617" }}>
      <Particles />

      {/* ── HEADER ─────────────────────────────────────────── */}
      <header className="relative z-10 flex items-center justify-between px-8 py-5 border-b border-purple-500/20">
        <div className="flex items-center gap-4">
          <div className="relative w-10 h-10 pulse-ring">
            <div className="w-10 h-10 rounded-full bg-gradient-to-br from-purple-600 to-pink-600 flex items-center justify-center">
              <span className="orbitron font-black text-sm">NX</span>
            </div>
          </div>
          <div>
            <div className="orbitron font-black text-xl glow-purple tracking-widest">NEXUS RECRUIT</div>
            <div className="mono text-xs text-purple-400 tracking-widest">HUNTER INTELLIGENCE SYSTEM v2.0</div>
          </div>
        </div>
        <nav className="flex gap-6 text-sm text-slate-400 tracking-widest uppercase">
          <button className="hover:text-purple-400 transition-colors">Overview</button>
          <button className="hover:text-purple-400 transition-colors">Archive</button>
          <button className="hover:text-purple-400 transition-colors">Settings</button>
        </nav>
      </header>

      <main className="relative z-10 max-w-7xl mx-auto px-6 py-10">

        {/* ── INPUT GATE ─────────────────────────────────────── */}
        <div className="panel rounded-2xl p-8 mb-10 box-glow-purple">
          <div className="flex items-center gap-4 mb-8">
            <div className="w-1 h-10 bg-gradient-to-b from-purple-500 to-pink-500 rounded" />
            <div>
              <h1 className="orbitron text-3xl font-black glow-purple">CANDIDATE SCANNER</h1>
              <p className="mono text-slate-400 text-sm mt-1">HUNTER'S GATE — INITIATE PROFILE SCAN</p>
            </div>
          </div>

          {error && (
            <div className="mb-6 p-4 rounded-lg border border-red-500/50 bg-red-900/20 mono text-red-400 text-sm">
              ⚠ {error}
            </div>
          )}

          <div className="grid grid-cols-1 md:grid-cols-2 gap-5 mb-6">
            {/* GitHub */}
            <div>
              <label className="mono text-xs text-purple-400 tracking-widest uppercase mb-2 block">◈ GitHub Username</label>
              <input
                type="text"
                value={githubUsername}
                onChange={(e) => setGithubUsername(e.target.value)}
                placeholder="octocat"
                className="nexus-input w-full rounded-lg px-4 py-3"
              />
            </div>

            {/* LinkedIn */}
            <div>
              <label className="mono text-xs text-cyan-400 tracking-widest uppercase mb-2 block">◈ LinkedIn URL</label>
              <input
                type="text"
                value={linkedinUrl}
                onChange={(e) => setLinkedinUrl(e.target.value)}
                placeholder="linkedin.com/in/username"
                className="nexus-input w-full rounded-lg px-4 py-3"
              />
            </div>

            {/* Role */}
            <div>
              <label className="mono text-xs text-pink-400 tracking-widest uppercase mb-2 block">◈ Target Role</label>
              <input
                type="text"
                value={role}
                onChange={(e) => setRole(e.target.value)}
                placeholder="Senior Backend Engineer"
                className="nexus-input w-full rounded-lg px-4 py-3"
              />
            </div>

            {/* Resume drop zone */}
            <div>
              <label className="mono text-xs text-yellow-400 tracking-widest uppercase mb-2 block">◈ Resume Upload (PDF)</label>
              <div
                onDragOver={(e) => { e.preventDefault(); setDragging(true); }}
                onDragLeave={() => setDragging(false)}
                onDrop={handleDrop}
                onClick={() => document.getElementById("file-input").click()}
                className={`nexus-input rounded-lg px-4 py-4 cursor-pointer text-center transition-all ${
                  dragging ? "border-yellow-400 bg-yellow-900/20" : ""
                } ${resume ? "border-green-500/50 bg-green-900/10" : ""}`}
              >
                {resume ? (
                  <span className="text-green-400 mono text-sm">✓ {resume.name}</span>
                ) : (
                  <span className="text-slate-500 mono text-sm">
                    {dragging ? "Drop it here..." : "Drag & drop or click to upload"}
                  </span>
                )}
              </div>
              <input
                id="file-input"
                type="file"
                accept=".pdf"
                className="hidden"
                onChange={(e) => { if (e.target.files?.[0]) { setResume(e.target.files[0]); setError(""); } }}
              />
            </div>
          </div>

          <button
            onClick={fetchAnalysis}
            disabled={loading}
            className="btn-nexus relative px-10 py-4 rounded-xl font-bold tracking-widest uppercase orbitron text-sm
              bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500
              disabled:opacity-40 disabled:cursor-not-allowed transition-all
              box-glow-purple"
          >
            {loading ? (
              <span className="flex items-center gap-3">
                <span className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full inline-block" style={{ animation: "spin 0.8s linear infinite" }} />
                SCANNING...
              </span>
            ) : (
              "⚡ INITIATE SCAN"
            )}
          </button>
        </div>

        {/* ── LOADING ─────────────────────────────────────────── */}
        {loading && <ScanLoader />}

        {/* ── RESULTS DASHBOARD ──────────────────────────────── */}
        {!loading && data && (
          <>
            {/* Rank banner */}
            <div className="panel rounded-2xl p-6 mb-8 flex items-center justify-between float-in box-glow-purple">
              <div className="flex items-center gap-6">
                <div className="orbitron text-7xl font-black" style={{ fontFamily: "'Orbitron', monospace" }}>
                  <span className={rank.cls}>{rank.label}</span>
                </div>
                <div>
                  <div className={`orbitron text-2xl font-black ${rank.cls}`}>{rank.title}</div>
                  <div className="mono text-slate-400 text-sm mt-1 tracking-widest">
                    TARGET ROLE: <span className="text-purple-300">{role.toUpperCase()}</span>
                  </div>
                </div>
              </div>
              <div className={`px-6 py-3 rounded-xl border font-bold orbitron tracking-widest text-sm ${
                data.recommendation === "Strong Hire"
                  ? "border-green-500/50 bg-green-900/20 text-green-400"
                  : data.recommendation === "Weak Hire"
                  ? "border-yellow-500/50 bg-yellow-900/20 text-yellow-400"
                  : "border-red-500/50 bg-red-900/20 text-red-400"
              }`}>
                {data.recommendation === "Strong Hire" ? "✅" : data.recommendation === "Weak Hire" ? "⚠️" : "❌"}{" "}
                {data.recommendation.toUpperCase()}
              </div>
            </div>

            {/* Score cards */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
              <StatCard label="Candidate Score"    value={data.candidateScore}       color="purple" icon="⚔️"  delay="delay-1" />
              <StatCard label="Skill Match"        value={data.skillMatch}           color="cyan"   icon="🎯"  delay="delay-2" />
              <StatCard label="Authenticity"       value={data.authenticity}         color="pink"   icon="💎"  delay="delay-3" />
              <StatCard label="Activity Streak"    value={data.activityConsistency}  color="gold"   icon="⚡"  delay="delay-4" />
            </div>

            {/* XP bar */}
            <div className="panel rounded-xl p-5 mb-8 float-in delay-5">
              <div className="flex justify-between items-center mb-3">
                <span className="orbitron text-sm tracking-widest text-slate-400">OVERALL XP PROGRESS</span>
                <span className="mono text-purple-400">{data.candidateScore} / 100 XP</span>
              </div>
              <div className="h-3 bg-slate-800 rounded-full overflow-hidden">
                <div
                  className="h-full xp-bar rounded-full"
                  style={{ "--target-width": `${data.candidateScore}%`, width: "0%" }}
                />
              </div>
            </div>

            {/* Main grid */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
              {/* Skills breakdown */}
              <div className="md:col-span-2 panel rounded-2xl p-7 float-in delay-1">
                <div className="flex items-center gap-3 mb-7">
                  <span className="text-xl">🧠</span>
                  <h3 className="orbitron font-bold text-lg tracking-widest glow-purple">SKILL POWER LEVELS</h3>
                </div>
                <div className="space-y-5">
                  {data.skillsBreakdown.map((skill, i) => (
                    <SkillBar key={i} name={skill.name} value={skill.value} index={i} />
                  ))}
                </div>
              </div>

              {/* Platforms */}
              <div className="panel rounded-2xl p-7 float-in delay-2">
                <div className="flex items-center gap-3 mb-7">
                  <span className="text-xl">🌐</span>
                  <h3 className="orbitron font-bold text-lg tracking-widest glow-cyan">PLATFORM DATA</h3>
                </div>
                <div className="space-y-5">
                  {data.platforms.map((p, i) => (
                    <div key={i} className="flex items-center justify-between p-4 rounded-xl bg-slate-800/50 border border-slate-700/50">
                      <span className="text-slate-300 font-semibold">{p.name}</span>
                      <span className="mono text-cyan-400 text-sm">{p.value}</span>
                    </div>
                  ))}
                  {/* Decorative stats */}
                  <div className="mt-4 p-4 rounded-xl bg-gradient-to-br from-purple-900/30 to-pink-900/20 border border-purple-500/20">
                    <div className="mono text-xs text-slate-400 mb-1 tracking-widest">ANALYSIS COMPLETE</div>
                    <div className="orbitron text-purple-400 font-bold">Multi-Source Verified</div>
                  </div>
                </div>
              </div>
            </div>

            {/* Commit chart */}
            <div className="panel rounded-2xl p-7 mb-8 float-in delay-3">
              <div className="flex items-center justify-between mb-2">
                <div className="flex items-center gap-3">
                  <span className="text-xl">💻</span>
                  <h3 className="orbitron font-bold text-lg tracking-widest glow-pink">COMMIT BATTLE HISTORY</h3>
                </div>
                <span className="mono text-xs text-slate-500 tracking-widest">LAST 6 MONTHS</span>
              </div>
              <CommitChart data={data.githubActivity} />
            </div>

            {/* Interview questions */}
            <div className="panel rounded-2xl p-7 float-in delay-4">
              <div className="flex items-center gap-3 mb-7">
                <span className="text-xl">⚔️</span>
                <h3 className="orbitron font-bold text-xl tracking-widest glow-gold">BATTLE ARENA — INTERVIEW CHALLENGES</h3>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {data.interviewQuestions.map((q, i) => {
                  const levels = ["LEVEL 1: STARTER", "LEVEL 2: ADVANCED", "LEVEL 3: EXPERT", "LEVEL 4: BOSS", "LEVEL 5: RAID"];
                  const colors = [
                    "border-green-500/40 bg-green-900/10",
                    "border-cyan-500/40 bg-cyan-900/10",
                    "border-purple-500/40 bg-purple-900/10",
                    "border-pink-500/40 bg-pink-900/10",
                    "border-yellow-500/40 bg-yellow-900/10",
                  ];
                  const textColors = ["text-green-400", "text-cyan-400", "text-purple-400", "text-pink-400", "text-yellow-400"];
                  return (
                    <div
                      key={i}
                      className={`p-5 rounded-xl border ${colors[i % 5]} lift slide-up`}
                      style={{ animationDelay: `${i * 100}ms`, opacity: 0 }}
                    >
                      <div className={`orbitron text-xs font-bold mb-3 tracking-widest ${textColors[i % 5]}`}>
                        {levels[i % 5]}
                      </div>
                      <p className="text-slate-200 text-sm leading-relaxed">{q}</p>
                    </div>
                  );
                })}
              </div>
            </div>
          </>
        )}

        {/* ── EMPTY STATE ─────────────────────────────────────── */}
        {!loading && !data && (
          <div className="text-center py-28 float-in">
            <div className="relative inline-block mb-8">
              <div className="w-28 h-28 rounded-full bg-gradient-to-br from-purple-900/60 to-pink-900/40 border border-purple-500/30 flex items-center justify-center mx-auto">
                <span className="text-5xl">🎯</span>
              </div>
              <div className="absolute inset-0 rounded-full border border-purple-500/20 animate-ping" />
            </div>
            <h2 className="orbitron text-3xl font-black glow-purple mb-3">HUNTER'S GATE AWAITS</h2>
            <p className="mono text-slate-400 text-sm tracking-widest">ENTER CANDIDATE DATA TO INITIATE SCAN SEQUENCE</p>
            <div className="flex justify-center gap-8 mt-10 text-xs mono text-slate-600 tracking-widest">
              <span>◈ GITHUB</span>
              <span>◈ LINKEDIN</span>
              <span>◈ RESUME</span>
              <span>◈ ROLE</span>
            </div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="relative z-10 text-center py-6 border-t border-purple-500/10 mono text-xs text-slate-600 tracking-widest">
        NEXUS RECRUIT v2.0 — HUNTER INTELLIGENCE SYSTEM — ALL CANDIDATE DATA ENCRYPTED
      </footer>
    </div>
  );
}