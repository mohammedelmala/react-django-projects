import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Users from "./screens/Users";
import User from "./screens/User";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="" index element={<Users />} />
        <Route path="users/:id" element={<User />} />
      </Routes>
    </Router>
  );
};

export default App;
