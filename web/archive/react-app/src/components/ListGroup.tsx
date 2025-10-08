// This file a React component
// (indicated by tsx extension).
// By convention, a tsx file contains a function-based
// or class-based component that can be used inside other
// components like App.tsx.

// -----------IMPORTS-----------
import { MouseEvent, useState } from "react";

// -----------PROPERTIES-----------
// Properties (Props) specify the input for this component.
// When you initialize the component, you must specify its properties.
// Props are immutable and should not be changed inside functions.
// The syntax uses TypeScript -> paramterName: ParameterType
// The properties for this component are:
// - items: list of items to display
// - heading: the name of this list to display
// - onSelectItem: void function specifying what should happen when an item is selected
interface Props {
  items: string[];
  heading: string;
  onSelectItem: (item: string) => void;
}

// -----------FUNCTION-BASED COMPONENT-----------
// This component takes {items, heading, onSelectItem } properties
// and returns a list to display on a webpage.
// This component reads items, and convert them into list items to display.
function ListGroup({ items, heading, onSelectItem }: Props) {
  // example of a Hook, a built-in React function that allows function
  // components to access React features like state. This hook returns
  // a variable and a function to update the variable.
  const [selectedIndex, setSelectedIndex] = useState(-1);

  // Inside a React component, what looks like HTML is
  // actually JSX (JavaScript XML). In JSX, you can insert
  // standard HTML elements or other React components.
  // Or you can use curly braces to insert JS code.
  // ex: {JavaScript variable or function}
  // ex: {{objectKey: "objectValue"}}
  //
  // For conditional rendering, you could use ? or &&.
  // ex: rendering a custom paragraph if items is length 0
  //     {items.length === 0 ? <p>No items found</p> : null}
  //     {items.length === 0 && <p>No items found</p>}
  //
  // To give JSX elements a class, use the className property.
  // These JSX elements use Bootstrap classes.

  // In React, a component can only return one element
  // This has to do with the React engine, specifically the
  // react-dom dependency, which manages and renders the
  // "virtual DOM" (component tree)
  //
  // Workarounds:  wrap everything in a React <Fragment>
  // (need to import from react), or wrap everything in
  // empty tags <> (implicit Fragment)
  return (
    <>
      <h1>{heading}</h1>

      {items.length === 0 && <p>No items found</p>}

      <ul className="list-group">
        {/* Array.map creates a new array based on the calling array, 
        populating the array using the funciton inside map(). Here
        we use Array.map to convert items into List Items.*/}
        {items.map((item, index) => (
          <li
            className={
              selectedIndex === index
                ? "list-group-item active"
                : "list-group-item"
            }
            key={item}
            onClick={() => {
              setSelectedIndex(index);
              onSelectItem(item);
            }}
          >
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}

// This is boiler-plate JavaScript code to export a
//  component, so it can be imported by other files.
export default ListGroup;
