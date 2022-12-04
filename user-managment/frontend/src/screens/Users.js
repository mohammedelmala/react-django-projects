import { useState, useEffect } from "react";
import useFetch from "./useFetch";
import UserCard from "../components/UserCard";

const Users = () => {
  const { loading, data } = useFetch();
  const [users, setUsers] = useState([]);

  useEffect(() => {
    setUsers(data);
  }, [loading]);

  return (
    <main>
      <div className="section-title">
        <h2>Users</h2>
        <div className="underline" />
      </div>
      <section className="center">
        <div className="container">
          {!loading &&
            users.map((user, index) => {
              return <UserCard key={index} {...user} />;
            })}
        </div>
      </section>
    </main>
  );
};

export default Users;
