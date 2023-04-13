import React from 'react';
import axios from 'axios'

type Base64 = string;

export default class Post extends React.Component {

    render(): React.ReactNode {
        console.log("I HAVE MADE A BIG THINGY");
        let images: Array<Base64> = [];
        axios.get(`http://127.0.0.1:8000/`).then(res => {
            images = res.data;
            console.log(images);
        });
        return (
            <ul>
                asdofiajsodfij
                { images.map((image) => <img src={`data:image/jpeg;base64,${image}`} />)}
            </ul>
        )
    }
}