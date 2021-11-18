# Educational-practice
Отчёт по учебной практике c дневником https://docs.google.com/document/d/1Tqesmuk7lTAySsLWKVhUL-XP6ANGPOYy/edit?usp=sharing&ouid=115676966877108699403&rtpof=true&sd=true
Расписание https://docs.google.com/document/d/1PLtdWfjnK8BSZa300r2l6THs9LmolqKV/edit
Дневник https://docs.google.com/document/d/1zTGYvn0IrEx-MoH-GizGGwqugdgHYXZw/edit
Задания доступны по ссылке https://docs.google.com/presentation/d/17YdUQJrXn2dPckjSeDarp3v6mYDyaHhsLKEFe0GpqEk/edit#slide=id.p




#include <opencv2/core/utility.hpp>
#include "opencv2/videoio.hpp"
#include "opencv2/highgui.hpp"


using namespace cv;
using namespace std;

VideoCapture cap;
Mat frame;


int main(int argc, char* argv[]) {
cvNamedWindow("Example2", CV_WINDOW_AUTOSIZE);
{
	// получаем любую подключённую камеру
	CvCapture* capture = cvCaptureFromCAM(0); //cvCaptureFromCAM( 0 );
	assert(capture == 0);

	cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_WIDTH, 640);//1280); 
	cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_HEIGHT, 480);//960); 

	// узнаем ширину и высоту кадра
	double width = cvGetCaptureProperty(capture, CV_CAP_PROP_FRAME_WIDTH);
	double height = cvGetCaptureProperty(capture, CV_CAP_PROP_FRAME_HEIGHT);
	printf("[i] %.0f x %.0f\n", width, height);

	IplImage* frame=0;

	cvNamedWindow("capture", CV_WINDOW_AUTOSIZE);

	printf("[i] press Enter for capture image and Esc for quit!\n\n");

	int counter = 0;
	char filename[512];

	while (true) {
		// получаем кадр
		frame = cvQueryFrame(capture);

		// показываем
		cvShowImage("capture", frame);

		char c = cvWaitKey(33);
		if (c == 27) { // нажата ESC
			break;
		}
		else if (c == 13) { // Enter
			// сохраняем кадр в файл
			sprintf(filename, "Image%d.jpg", counter);
			printf("[i] capture... %s\n", filename);
			cvSaveImage(filename, frame);
			counter++;
		}
	}
	// освобождаем ресурсы
	cvReleaseCapture(&capture);
	cvDestroyWindow("Example2");
	return 0;
	CVAPI() cvSaveImage(const char* filename, const CvArr * image, const int* params CV_DEFAULT(0));
