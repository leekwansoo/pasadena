import firebase from 'firebase/app';
import 'firebase/storage';
import 'firebase/firestore';

// Your web app's Firebase configuration
var firebaseConfig = {
    apiKey: "AIzaSyA7VJJ0FifoLNNZuwz97sY8XCnpdH-iOuE",
    authDomain: "timebridge-2301.firebaseapp.com",
    databaseURL: "gs://timebridge-2301.appspot.com",
    projectId: "timebridge-2301",
    storageBucket: "timebridge-2301.appspot.com",
    messagingSenderId: "486255936313",
    appId: "1:486255936313:web:24fed97f8839d405821ee8",
    measurementId: "G-XJZY3Q76LL"
  };
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const projectStorage = firebase.storage();
const projectFirestore = firebase.firestore();
const timestamp = firebase.firestore.FieldValue.serverTimestamp;

export { projectStorage, projectFirestore, timestamp };