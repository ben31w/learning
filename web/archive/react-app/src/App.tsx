import { useState } from "react";
import Alert from "./components/Alert";
import Button from "./components/Button";
import ListGroup from "./components/ListGroup";

function App() {
  // ----------Variables----------
  let items = ["New York", "Rome", "Hanoi"];
  const [alertVisibility, setAlertVisibility] = useState(false);

  // ----------Event handlers (lambdas)----------
  const handleSelectItem = (item: string) => {
    console.log(item);
  };

  const handleClickRefresh = () => {
    location.reload();
  };

  const handleCloseAlert = () => {
    setAlertVisibility(false);
  };

  const handleOpenAlert = () => {
    setAlertVisibility(true);
  };

  // ----------Content----------
  return (
    <div>
      {alertVisibility && (
        <Alert onClose={handleCloseAlert}>
          <strong>My alert</strong>
        </Alert>
      )}

      <ListGroup
        items={items}
        heading="Cities"
        onSelectItem={handleSelectItem}
      />
      <Button onClick={handleClickRefresh}>Refresh</Button>
      <Button onClick={handleOpenAlert} type="danger">
        Create Alert
      </Button>
    </div>
  );
}

export default App;
