import React, { ReactNode } from 'react'

// Type is optional paramter specifying the type of button
interface Props {
    children: ReactNode;
    type?: 'primary' | 'secondary' | 'danger';
    onClick: () => void;
}

// Default type is primary
const Button = ({children, onClick, type='primary'}: Props) => {
  return (
    <button className={"btn btn-" + type} onClick={onClick}>{children}</button>
  )
}

export default Button