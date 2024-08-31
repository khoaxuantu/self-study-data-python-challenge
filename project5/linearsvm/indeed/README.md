<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Listing Spider and Email Sender</title>
</head>
<body>
    <h1>Job Listing Spider and Email Sender</h1>
    <ol>
        <li><strong>Crawler (search_spiders.py)</strong>: Một trình thu thập thông tin (crawler) sử dụng Scrapy để thu thập danh sách việc làm từ Indeed.</li>
        <li><strong>Email Sender (run_spider_scheduler.py)</strong>: Một tập tin Python để gửi email với tệp CSV kết quả thu thập thông tin.</li>
    </ol>
    <h2>Yêu cầu</h2>
    <p>Trước khi bắt đầu, hãy đảm bảo rằng bạn đã cài đặt các gói sau:</p>
    <ul>
        <li><code>scrapy</code></li>
        <li><code>requests</code></li>
        <li><code>beautifulsoup4</code></li>
        <li><code>w3lib</code></li>
        <li><code>apscheduler</code></li>
        <li><code>pandas</code></li>
        <li><code>smtplib</code> (có sẵn trong thư viện chuẩn Python)</li>
        <li><code>email</code> (có sẵn trong thư viện chuẩn Python)</li>
    </ul>
    <p>Bạn có thể cài đặt các gói phụ thuộc bằng cách sử dụng pip:</p>
    <pre><code>pip install scrapy requests beautifulsoup4 w3lib apscheduler pandas</code></pre>
    <h2>Cấu hình Mật khẩu Ứng dụng cho Gmail</h2>
    <p>Nếu bạn sử dụng Gmail và nhận được lỗi về mật khẩu không hợp lệ, bạn có thể cần tạo mật khẩu ứng dụng:</p>
    <ol>
        <li><strong>Bật Xác Thực Hai Bước</strong>:
            <ul>
                <li>Truy cập <a href="https://myaccount.google.com/security">Google Account Security</a>.</li>
                <li>Bật xác thực hai bước (Two-Step Verification).</li>
            </ul>
        </li>
        <li><strong>Tạo Mật khẩu Ứng dụng</strong>:
            <ul>
                <li>Trong phần Security, chọn <strong>App passwords</strong>.</li>
                <li>Chọn ứng dụng là Mail và thiết bị là Other (bạn có thể nhập tên tùy ý như "Python script").</li>
                <li>Nhấn Generate và sao chép mật khẩu ứng dụng.</li>
            </ul>
        </li>
        <li><strong>Sử dụng Mật khẩu Ứng dụng</strong>:
            <ul>
                <li>Thay thế mật khẩu tài khoản email bằng mật khẩu ứng dụng khi được yêu cầu.</li>
            </ul>
        </li>
    </ol>
    <h2>Cách sử dụng</h2>
    <ol>
        <li><strong>Chạy Trình Thu Thập Thông Tin</strong>:
            <p>Để thu thập danh sách việc làm từ Indeed, chạy lệnh sau:</p>
            <pre><code>scrapy crawl indeed_search</code></pre>
            <p>Lệnh này sẽ thực thi trình thu thập thông tin và lưu kết quả vào tệp CSV.</p>
        </li>
        <li><strong>Gửi Email</strong>:
            <p>Để gửi email với tệp CSV kết quả, chạy lệnh sau:</p>
            <pre><code>python run_spider_scheduler.py</code></pre>
            <p>Lệnh này sẽ gửi email chứa tệp CSV kết quả đến địa chỉ email đã cấu hình.</p>
        </li>
    </ol>
    <h2>Tài liệu thêm</h2>
    <ul>
        <li><a href="https://docs.scrapy.org/en/latest/">Scrapy Documentation</a></li>
        <li><a href="https://requests.readthedocs.io/en/latest/">Requests Documentation</a></li>
        <li><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup Documentation</a></li>
        <li><a href="https://w3lib.readthedocs.io/en/latest/">w3lib Documentation</a></li>
        <li><a href="https://apscheduler.readthedocs.io/en/latest/">APScheduler Documentation</a></li>
        <li><a href="https://pandas.pydata.org/pandas-docs/stable/">Pandas Documentation</a></li>
        <li><a href="https://docs.python.org/3/library/email.html">Python Email Documentation</a></li>
    </ul>
</body>
</html>
