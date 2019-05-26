var config = {
    apiKey: "AIzaSyDlSw84Pzt8KYCqHzHsoDc9nYmwHUuN0Rk",
    authDomain: "sftc-6b9fd.firebaseapp.com",
    databaseURL: "https://sftc-6b9fd.firebaseio.com",
    projectId: "sftc-6b9fd",
    storageBucket: "sftc-6b9fd.appspot.com",
    messagingSenderId: "333564706845"
  };
  firebase.initializeApp(config);
firebase.auth().onAuthStateChanged(function(user) {
    if (user) {
      console.log('login successful')
    }
  });