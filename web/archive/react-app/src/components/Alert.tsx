// Using the children prop enables you to put HTML code
// between a component's tags.

import { ReactNode } from "react";

interface Prop {
  children: ReactNode;
  onClose: () => void;
}

// Create a yellow alert with some text and a close button. 
// children contains the text of this alert.
// onClose is the function called when this alert is closed.
function Alert({ children, onClose }: Prop) {
  return (
    <div
      className="alert alert-warning alert-dismissible fade show"
      role="alert"
    >
      {children}
      <button
        type="button"
        className="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
        onClick={onClose}
      ></button>
    </div>
  );
}

export default Alert;
