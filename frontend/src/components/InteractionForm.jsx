import { useState } from "react";
import api from "../services/api";

function InteractionForm() {

  const [form, setForm] = useState({
    hcp_id: "",
    interaction_type: "",
    notes: ""
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

      await api.post("/interaction/", {
        ...form,
        hcp_id: Number(form.hcp_id)
      });

      alert("Interaction Logged Successfully!");

      setForm({
        hcp_id: "",
        interaction_type: "",
        notes: ""
      });

    } catch (error) {
      console.log(error.response?.data);
      alert("Error Logging Interaction");
    }
  };


  return (
    <div>

      <h2>Log Interaction</h2>

      <form onSubmit={handleSubmit}>

        <input
          name="hcp_id"
          placeholder="HCP ID"
          value={form.hcp_id}
          onChange={handleChange}
        />

        <br /><br />


        <input
          name="interaction_type"
          placeholder="Meeting Type"
          value={form.interaction_type}
          onChange={handleChange}
        />

        <br /><br />


        <textarea
          name="notes"
          placeholder="Meeting Notes"
          value={form.notes}
          onChange={handleChange}
        />

        <br /><br />


        <button type="submit">
          Save Interaction
        </button>


      </form>

    </div>
  );
}

export default InteractionForm;
