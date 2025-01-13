// src/pages/ChatbotPage.jsx
import { useState } from 'react';
import { Button, TextField, Typography, Box, AppBar, Toolbar, List, ListItem, ListItemText, CircularProgress } from '@mui/material';
import ApiChatbot from '../utils/api/chatbot'; // Assume this handles chatbot-related API calls
import { toast } from 'react-toastify';

function ChatbotPage() {
  const [userInput, setUserInput] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  // Handle user input submission
  const handleSendMessage = async () => {
    if (!userInput.trim()) {
      toast.error('Please enter a message.');
      return;
    }

    // Add user message to chat history
    const newChatHistory = [...chatHistory, { role: 'user', content: userInput }];
    setChatHistory(newChatHistory);
    setUserInput('');
    setLoading(true);

    try {
      // Send message to chatbot API
      const response = await ApiChatbot.postChatbotResponse({ messages: newChatHistory });
      if (response.success) {
        // Add chatbot response to chat history
        setChatHistory([...newChatHistory, { role: 'chatbot', content: response.message }]);
      } else {
        toast.error('Failed to get response from chatbot.');
      }
    } catch (error) {
      console.error(error);
      toast.error('An error occurred while communicating with the chatbot.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box sx={{ padding: '20px' }}>
      {/* Header */}
      <AppBar position="sticky">
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            Chatbot
          </Typography>
          <Button variant="contained" color="secondary" href="/candidate-management">
            Back to Candidate Management
          </Button>
        </Toolbar>
      </AppBar>

      {/* Chat Interface */}
      <Box mt={2} sx={{ display: 'flex', flexDirection: 'column', height: 'calc(100vh - 64px)' }}>
        {/* Chat History */}
        <Box sx={{ flexGrow: 1, overflowY: 'auto', border: '1px solid #ccc', borderRadius: '4px', padding: '10px' }}>
          <List>
            {chatHistory.map((message, index) => (
              <ListItem key={index} alignItems="flex-start">
                <ListItemText
                  primary={message.role === 'user' ? 'You' : 'Chatbot'}
                  secondary={message.content}
                />
              </ListItem>
            ))}
          </List>
          {loading && (
            <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '10px' }}>
              <CircularProgress size={24} />
            </Box>
          )}
        </Box>

        {/* Input Box */}
        <Box mt={2} sx={{ display: 'flex', alignItems: 'center' }}>
          <TextField
            fullWidth
            variant="outlined"
            placeholder="Type your message here..."
            value={userInput}
            onChange={(e) => setUserInput(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === 'Enter') handleSendMessage();
            }}
          />
          <Button
            variant="contained"
            color="primary"
            onClick={handleSendMessage}
            sx={{ marginLeft: '10px' }}
          >
            Send
          </Button>
        </Box>
      </Box>
    </Box>
  );
}

export default ChatbotPage;
