import React from 'react';
import axios from 'axios'

type Base64 = string;

export default class Post extends React.Component {
    state: { data: Array<Base64> } = { data: [] };

    componentDidMount(): void {
        axios.get(`http://127.0.0.1:8000/`).then(res => {
            this.setState(res.data);
            console.log(res.data, this.state);
            this.forceUpdate();
        });
    }

    render(): React.ReactNode {
        return (
            <ul>
                { this.state.data.map((image) => <img key={`${image.slice(image.length-10)}`} src={`data:image/jpeg;base64,${image}`} alt="alternative content" />)}
            </ul>
        )
    }
}