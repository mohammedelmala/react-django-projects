import { Link } from "react-router-dom";

const UserCard = ({ id, username, email, profile_picture }) => {
  return (
    <div className="card">
      <img src={profile_picture} alt={username} />
      <h3>{username}</h3>
      <p>{email}</p>
      <Link className="btn" to={`/users/${id}`}>
        view profile
      </Link>
    </div>
  );
};

export default UserCard;
