/**
 *
 * @param {object} param
 * @param {number} param.size
 * @returns {JSX.Element}
 */
export function UserIcon({ size = 25 }) {
  return (
    <svg
      width={`${size}`}
      height={`${size}`}
      viewBox="0 0 25 25"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <g clipPath="url(#clip0_177_891)">
        <path
          d="M12.5 12.5C13.7361 12.5 14.9445 12.1334 15.9723 11.4467C17.0001 10.7599 17.8012 9.78381 18.2742 8.64177C18.7473 7.49974 18.8711 6.24307 18.6299 5.03069C18.3888 3.81831 17.7935 2.70466 16.9194 1.83059C16.0453 0.956507 14.9317 0.361252 13.7193 0.120095C12.5069 -0.121063 11.2503 0.00270804 10.1082 0.475756C8.96619 0.948803 7.99007 1.74988 7.30331 2.77769C6.61656 3.8055 6.25 5.01387 6.25 6.25C6.25165 7.9071 6.91067 9.49585 8.08241 10.6676C9.25415 11.8393 10.8429 12.4983 12.5 12.5ZM12.5 2.08334C13.3241 2.08334 14.1297 2.32771 14.8149 2.78555C15.5001 3.24339 16.0341 3.89413 16.3495 4.65549C16.6649 5.41685 16.7474 6.25462 16.5866 7.06288C16.4258 7.87113 16.029 8.61356 15.4463 9.19628C14.8636 9.779 14.1211 10.1758 13.3129 10.3366C12.5046 10.4974 11.6668 10.4149 10.9055 10.0995C10.1441 9.78414 9.49338 9.25008 9.03554 8.56488C8.5777 7.87967 8.33333 7.07409 8.33333 6.25C8.33333 5.14493 8.77232 4.08513 9.55372 3.30372C10.3351 2.52232 11.3949 2.08334 12.5 2.08334Z"
          fill="black"
        />
        <path
          d="M12.5 14.5833C10.0144 14.586 7.63147 15.5746 5.87392 17.3322C4.11636 19.0897 3.12776 21.4727 3.125 23.9583C3.125 24.2345 3.23475 24.4995 3.4301 24.6948C3.62545 24.8902 3.8904 24.9999 4.16667 24.9999C4.44293 24.9999 4.70789 24.8902 4.90324 24.6948C5.09859 24.4995 5.20833 24.2345 5.20833 23.9583C5.20833 22.0244 5.97656 20.1697 7.34401 18.8023C8.71147 17.4348 10.5661 16.6666 12.5 16.6666C14.4339 16.6666 16.2885 17.4348 17.656 18.8023C19.0234 20.1697 19.7917 22.0244 19.7917 23.9583C19.7917 24.2345 19.9014 24.4995 20.0968 24.6948C20.2921 24.8902 20.5571 24.9999 20.8333 24.9999C21.1096 24.9999 21.3746 24.8902 21.5699 24.6948C21.7653 24.4995 21.875 24.2345 21.875 23.9583C21.8722 21.4727 20.8836 19.0897 19.1261 17.3322C17.3685 15.5746 14.9856 14.586 12.5 14.5833Z"
          fill="black"
        />
      </g>
    </svg>
  );
}