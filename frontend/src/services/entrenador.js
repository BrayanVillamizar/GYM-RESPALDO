import axios from "axios";

/**
 * @typedef {Object} Client
 * @property {string} nombre
 * @property {string} identificacion
 * @property {string} telefono
 * @property {string} sexo
 */

/**
 * 
 * @param {string} token 
 * @returns {Promise<Client[]>}
 * @throws {Error}
 */
export function getClientesActivos(token) {
  return axios
  .get('http://localhost:8888/entrenador/clientes_activos', {
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
  })
  .then(({ data, status }) => {
    if (status === 200) {
      return (data.resultado ?? []).map((client) => ({
          nombre: client.nombre,
          identificacion: client['ID_cliente'],
          telefono: client.telefono,
          sexo: client.sexo,
        }));
    } else {
      console.error(data);
      throw new Error('Error al cargar los datos');
    }
  })
  .catch((error) => {
    if (error.response?.status === 404) return [];
    console.error(error);
    throw new Error('Error al cargar los datos');
  });
}
