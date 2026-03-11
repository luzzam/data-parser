
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

