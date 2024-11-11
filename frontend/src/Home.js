import React, {useState, useEffect} from "react";
import {Link} from "react-router-dom";
import axios from "axios";
import {jwtDecode} from 'jwt-decode';
import {Helmet} from "react-helmet"
import {toast} from 'react-toastify'
import "./Home.css";

document.documentElement.lang = "es";

export default function Home(props) {

    const frases = {1: "El único mal entrenamiento es el que no haces",
                    2: "No se trata de ser el mejor, sino de ser mejor que ayer",
                    3: "Cada repetición cuenta, cada esfuerzo te acerca a tus metas",
                    4: "No te detengas cuando estés cansado, detente cuando hayas terminado",
                    5: "Cada gota de sudor es un paso hacia tu mejor versión"
                    }
    const [user, setUser] = useState({}); //Sirve para los datos del usuario
    const [auth_token, setToken] = useState(); //Sirve para los datos del token
    const [rango_token, setRango] = useState(); //Sirve para los datos del rango

    useEffect(() => {
        const auth_token = localStorage.getItem("auth_token"); //Cargo del token del almacenamiento local
        setToken(auth_token);
        if(auth_token != null) { //Verifica si el token existe

            const decoded_token = jwtDecode(auth_token);
            const current_time = Date.now() / 1000;

            if(decoded_token.exp > current_time){ //Verifica si el token no ha expirado
                const auth_token_type = localStorage.getItem("auth_token_type");
                const token_usuario = auth_token_type + " " + auth_token;

                const rango_token = decoded_token.Rango //Recupera rango del token
                setRango(rango_token)
                console.log(rango_token) //Sólo sirve para pruebas

                //Obtiene datos de la API
                axios.get("http://localhost:8888/cliente/", {headers: {Authorization: token_usuario}}).then((response) => {
                    console.log(response); //Sólo sirve para pruebas
                    setUser(response.data.resultado);
                }).catch((error) => {
                    console.log(error); //Sólo sirve para pruebas
                })
            } else {
                localStorage.removeItem("auth_token")
                localStorage.removeItem("auth_token_type")
                toast.error("Token expirado")
            }
        }
    }, [auth_token])

    const paginas = () => {
        if (auth_token == null) {
            return(
                <div className="home_page">
                    <Helmet>
                        <meta charSet="utf-8"/>
                        <title>Gymcontrol - Príncipal</title>
                    </Helmet>
                    {frases[Math.floor(Math.random() * 5) + 1]}
                    <Link to="/?login"
                        onClick={() => {
                            props.setPage("login");
                        }}
                    >
                        <button type="button" className="btn btn-primary">Únete</button>
                    </Link>
                </div>
            );
        } else {
                return (
                    <div className="home_page">
                        <Helmet>
                            <meta charSet="utf-8"/>
                            <title>Gymcontrol - Príncipal</title>
                        </Helmet>
                        ¡BIENVENID{user.sexo === "MASCULINO" ? "O " : "A "} {rango_token === "Cliente" ? user.nombre : rango_token}!
                    </div>
                );;
        }
    };

    return <React.Fragment>{paginas()}</React.Fragment>;
}