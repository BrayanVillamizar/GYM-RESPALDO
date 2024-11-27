/**
 *
 * @param {object} param
 * @param {number} param.size
 * @returns {JSX.Element}
 */
export function UserIcon({ size }) {
  return (
    <svg
      width={`${size}`}
      height={`${size}`}
      viewBox="0 0 25 25"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <g clipPath="url(#clip0_177_916)">
        <path
          d="M19.7917 4.16667H15.625V3.125C15.625 2.2962 15.2958 1.50134 14.7097 0.915291C14.1237 0.32924 13.3288 0 12.5 0C11.6712 0 10.8763 0.32924 10.2903 0.915291C9.70424 1.50134 9.375 2.2962 9.375 3.125V4.16667H5.20833C3.82751 4.16832 2.50371 4.71759 1.52731 5.69398C0.550919 6.67037 0.00165402 7.99417 0 9.375L0 19.7917C0.00165402 21.1725 0.550919 22.4963 1.52731 23.4727C2.50371 24.4491 3.82751 24.9983 5.20833 25H19.7917C21.1725 24.9983 22.4963 24.4491 23.4727 23.4727C24.4491 22.4963 24.9983 21.1725 25 19.7917V9.375C24.9983 7.99417 24.4491 6.67037 23.4727 5.69398C22.4963 4.71759 21.1725 4.16832 19.7917 4.16667ZM11.4583 3.125C11.4583 2.84873 11.5681 2.58378 11.7634 2.38843C11.9588 2.19308 12.2237 2.08333 12.5 2.08333C12.7763 2.08333 13.0412 2.19308 13.2366 2.38843C13.4319 2.58378 13.5417 2.84873 13.5417 3.125V5.20833C13.5417 5.4846 13.4319 5.74955 13.2366 5.9449C13.0412 6.14025 12.7763 6.25 12.5 6.25C12.2237 6.25 11.9588 6.14025 11.7634 5.9449C11.5681 5.74955 11.4583 5.4846 11.4583 5.20833V3.125ZM22.9167 19.7917C22.9167 20.6205 22.5874 21.4153 22.0014 22.0014C21.4153 22.5874 20.6205 22.9167 19.7917 22.9167H5.20833C4.37953 22.9167 3.58468 22.5874 2.99862 22.0014C2.41257 21.4153 2.08333 20.6205 2.08333 19.7917V9.375C2.08333 8.5462 2.41257 7.75134 2.99862 7.16529C3.58468 6.57924 4.37953 6.25 5.20833 6.25H9.56667C9.7788 6.8589 10.1752 7.3867 10.7008 7.76018C11.2264 8.13366 11.8552 8.33432 12.5 8.33432C13.1448 8.33432 13.7736 8.13366 14.2992 7.76018C14.8248 7.3867 15.2212 6.8589 15.4333 6.25H19.7917C20.6205 6.25 21.4153 6.57924 22.0014 7.16529C22.5874 7.75134 22.9167 8.5462 22.9167 9.375V19.7917ZM10.4167 10.4167H5.20833C4.93207 10.4167 4.66711 10.5264 4.47176 10.7218C4.27641 10.9171 4.16667 11.1821 4.16667 11.4583V19.7917C4.16667 20.0679 4.27641 20.3329 4.47176 20.5282C4.66711 20.7236 4.93207 20.8333 5.20833 20.8333H10.4167C10.6929 20.8333 10.9579 20.7236 11.1532 20.5282C11.3486 20.3329 11.4583 20.0679 11.4583 19.7917V11.4583C11.4583 11.1821 11.3486 10.9171 11.1532 10.7218C10.9579 10.5264 10.6929 10.4167 10.4167 10.4167ZM9.375 18.75H6.25V12.5H9.375V18.75ZM20.8333 15.625C20.8333 15.9013 20.7236 16.1662 20.5282 16.3616C20.3329 16.5569 20.0679 16.6667 19.7917 16.6667H14.5833C14.3071 16.6667 14.0421 16.5569 13.8468 16.3616C13.6514 16.1662 13.5417 15.9013 13.5417 15.625C13.5417 15.3487 13.6514 15.0838 13.8468 14.8884C14.0421 14.6931 14.3071 14.5833 14.5833 14.5833H19.7917C20.0679 14.5833 20.3329 14.6931 20.5282 14.8884C20.7236 15.0838 20.8333 15.3487 20.8333 15.625ZM20.8333 11.4583C20.8333 11.7346 20.7236 11.9996 20.5282 12.1949C20.3329 12.3903 20.0679 12.5 19.7917 12.5H14.5833C14.3071 12.5 14.0421 12.3903 13.8468 12.1949C13.6514 11.9996 13.5417 11.7346 13.5417 11.4583C13.5417 11.1821 13.6514 10.9171 13.8468 10.7218C14.0421 10.5264 14.3071 10.4167 14.5833 10.4167H19.7917C20.0679 10.4167 20.3329 10.5264 20.5282 10.7218C20.7236 10.9171 20.8333 11.1821 20.8333 11.4583ZM18.75 19.7917C18.75 20.0679 18.6403 20.3329 18.4449 20.5282C18.2496 20.7236 17.9846 20.8333 17.7083 20.8333H14.5833C14.3071 20.8333 14.0421 20.7236 13.8468 20.5282C13.6514 20.3329 13.5417 20.0679 13.5417 19.7917C13.5417 19.5154 13.6514 19.2504 13.8468 19.0551C14.0421 18.8597 14.3071 18.75 14.5833 18.75H17.7083C17.9846 18.75 18.2496 18.8597 18.4449 19.0551C18.6403 19.2504 18.75 19.5154 18.75 19.7917Z"
          fill="black"
        />
      </g>
    </svg>
  );
}
