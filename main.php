<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width], initial-scale=1.0, user-scalable=no">
    <title>Meeter</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <a href="#">
            <img src="data/user.png" alt="user">
            <p>username</p>
        </a>
        <img src="data/Meeter_gray.png" alt="meeter">
    </header>
    <main>
        <div class="rooms">
            <dl>
                <dt>Direct Messages</dt>
                    <!-- using <dd></dd> with <a> inside to open a chat on the right side-->
                <dt>Rooms</dt>
                    <!-- using <dd></dd> with <a> inside to open a chat on the right side-->
            </dl>
        </div>
        <div class="chat">
            <div class="chat-box">
                <!-- some chat code stuff, mostly reading records from the database at server/database.db -->
            </div>
            <input type="text" placeholder="type:">
        </div>
    </main>
    <footer>
        <div>
            <img src="data/Meeter.png" alt="meeter">
            <p>meeter a.0.1</p>
        </div>
        <p>thank you for using meeter</p>
    </footer>
</body>
</html>
