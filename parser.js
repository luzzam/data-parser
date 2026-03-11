
export const getUrlParams = (url) => {
  const params = {};
  new URLSearchParams(new URL(url).search).forEach((value, key) => {
    params[key] = value;
  });
  return params;
};


const calculateDelay = (retryCount) => {
    return Math.pow(2, retryCount) * 1000;
};


export const generateRandomToken = (length = 32) => {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let token = '';
  for (let i = 0; i < length; i++) {
    token += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return token;
};

