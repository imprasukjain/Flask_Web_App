# ML Gender Detection Web App

This is a machine learning-based gender detection web application developed using Flask framework. The application utilizes a pre-trained deep learning model to predict the gender of individuals based on their facial features.

## Features

- Gender prediction: The application uses a deep learning model to analyze facial features and predict the gender of individuals.
- Real-time detection: Users can upload an image or use their device's camera to capture a live image for gender prediction.
- User-friendly interface: The web interface is designed to be intuitive and user-friendly, allowing users to easily interact with the application.
- Fast and accurate predictions: The deep learning model used in the application has been trained on a large dataset, resulting in fast and accurate gender predictions.
- Responsive design: The application is responsive and adapts to different screen sizes, ensuring a consistent user experience across devices.

## Demo

A live demo of the application can be accessed [here](https://your-app-url).

## Installation

To run the application locally, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/imprasukjain/Flask_Web_App.git
   ```

2. Navigate to the project directory:

   ```shell
   cd apps
   ```

3. Create a virtual environment:

   ```shell
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   ```shell
   source venv/bin/activate
   ```

5. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Run the application:

   ```shell
   python app.py
   ```

7. Open your web browser and visit `http://localhost:5000` to access the application.

## Usage

1. On the gender page, click on the "Choose File" button to upload an image or click on the "Use Camera" button to capture a live image.

2. If you chose to upload an image, select the desired image from your local machine.

3. Once an image is selected or captured, click on the "Predict" button to initiate the gender prediction.

4. Wait for the application to process the image and display the predicted gender on the screen.

5. To perform another prediction, click on the "Upload" button again.

## Model and Training

The gender detection model used in this application has been trained on a large dataset of labeled images.

The training process involved data preprocessing, model architecture design, and optimization techniques. The model achieved high accuracy and generalization capabilities on the validation and test sets.

For more details on the model architecture and training process, please refer to this [Repo](https://github.com/imprasukjain/Face-Recognition-Model).

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [GNU Affero General Public License v3.0 ](LICENSE).

## Acknowledgments

This application was developed with the help of the following open-source libraries and frameworks:

- Flask: [https://flask.palletsprojects.com](https://flask.palletsprojects.com)
- OpenCV: [https://opencv.org](https://opencv.org)
