// Thanks:
// https://dev.to/alanwest/how-to-build-a-real-time-chat-app-with-websockets-and-why-it-works-3m54
//
// Don't forget to install WebSocket from NPM
// npm i ws
//
// node server.js

const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

// Track all connected clients
const clients = new Set();

wss.on('connection', (ws) => {
  clients.add(ws);
  console.log(`Client connected. Total: ${clients.size}`);

  ws.on('message', (data) => {
    const message = data.toString();
    // Broadcast to every client except the sender
    for (const client of clients) {
      if (client !== ws && client.readyState === 1) {
        client.send(message);
      }
    }
  });

  ws.on('close', () => {
    clients.delete(ws);
    console.log(`Client disconnected. Total: ${clients.size}`);
  });
});

console.log('WebSocket server running on ws://localhost:8080');