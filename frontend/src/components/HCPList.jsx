import { useEffect, useState } from "react";
import api from "../services/api";


function HCPList() {

  const [hcps, setHcps] = useState([]);


  const fetchHCPs = async () => {

    try {

      const response = await api.get("/hcp/");

      setHcps(response.data);

    } catch (error) {

      console.log(error);

    }

  };


  useEffect(() => {

    fetchHCPs();

  }, []);



  return (

    <div>

      <h2>👨‍⚕️ Healthcare Professionals</h2>


      {
        hcps.map((hcp) => (

          <div className="card" key={hcp.id}>

            <h3>
              {hcp.name}
            </h3>


            <p>
              <b>Specialization:</b> {hcp.specialization}
            </p>


            <p>
              <b>Hospital:</b> {hcp.hospital}
            </p>


            <p>
              <b>City:</b> {hcp.city}
            </p>


            <p>
              <b>Email:</b> {hcp.email}
            </p>


            <p>
              <b>Phone:</b> {hcp.phone}
            </p>


          </div>

        ))
      }


    </div>

  );

}


export default HCPList;
