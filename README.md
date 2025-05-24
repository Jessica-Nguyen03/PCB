- Tải ultralytics
  
  !pip install ultralytics
  
Kết quả sau khi chạy mô hình

![image](https://github.com/user-attachments/assets/9f753920-bbca-4100-b5cd-0e9e54e6e843)

![image](https://github.com/user-attachments/assets/f2a9735e-869f-41c4-90b3-12d3b6bc0d87)


•	Sau khi huấn luyện mô hình YOLO, thu được được ghi nhận trên bảng kết quả sau khi huấn luyện các version. Cho thấy YOLOv8n có kết quả tốt nhất.
•	Tham số mAP50 của mô hình YOLOv8n đạt 99.3% nhỉnh hơn so với YOLOv11n 99.1%, cho thấy version 8 nhìn chung phát hiện chính xác hơn ở ngưỡng IoU ≥ 50.
•	Tham số mAP50-95 của mô hình YOLOv8n đạt 73.7% tiếp tục vượt trội so với YOLOv11n, thể hiện khả năng phát hiện ổn định qua dải IoU rộng (50%  95%). Đây là chỉ số quan trọng khi cần cân nhắc accuracy ở các trường hợp cần IoU cao.
•	Hai tham số Recall và Precision ở hai phiên bản đều rất cao (>98%), nhưng ở phiên bản YOLOv8n lại nhỉnh hơn cho thấy có lợi thế nhẹ trong việc tìm đủ đối tượng và giảm bớt cảnh báo sai.

# Demo model

![image](https://github.com/user-attachments/assets/b5e0777e-6dbd-4496-b306-94df49872e0f)



