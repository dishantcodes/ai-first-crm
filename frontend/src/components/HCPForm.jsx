import { useState } from "react";
import api from "../services/api";

function HCPForm() {

  const [form, setForm] = useState({
    name: "",
    specialization: "",
    hospital: "",
    city: "",
    email: "",
    phone: ""
  });


  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };


  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await api.post("/hcp/", form);

      alert("HCP Added Successfully!");

      setForm({
        name: "",
        specialization: "",
        hospital: "",
        city: "",
        email: "",
        phone: ""
      });

    } catch (error) {
  console.log("Full Error:", error);
  console.log("Response:", error.response);
  console.log("Data:", error.response?.data);

  alert(
    JSON.stringify(error.response?.data || error.message)
  );
}


  return (
    <div>

      <h2>Add HCP</h2>

      <form onSubmit={handleSubmit}>

        <input
          name="name"
          placeholder="Doctor Name"
          value={form.name}
          onChange={handleChange}
        />

        <br /><br />

        <input
          name="specialization"
          placeholder="Specialization"
          value={form.specialization}
          onChange={handleChange}
        />

        <br /><br />

        <input
          name="hospital"
          placeholder="Hospital"
          value={form.hospital}
          onChange={handleChange}
        />

        <br /><br />

        <input
          name="city"
          placeholder="City"
          value={form.city}
          onChange={handleChange}
        />

        <br /><br />

        <input
          name="email"
          placeholder="Email"
          value={form.email}
          onChange={handleChange}
        />

        <br /><br />

        <input
          name="phone"
          placeholder="Phone"
          value={form.phone}
          onChange={handleChange}
        />

        <br /><br />

        <button type="submit">
          Add HCP
        </button>

      </form>

    </div>
  );
}

export default HCPForm;
