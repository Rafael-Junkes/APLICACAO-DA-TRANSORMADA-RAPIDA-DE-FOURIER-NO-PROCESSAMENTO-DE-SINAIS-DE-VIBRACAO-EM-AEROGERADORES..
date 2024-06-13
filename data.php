<?php
$servername = "localhost";
$dbname = "vibraFFT";
$username = "pi";
$password = "raspberry";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT MPUtemp, mVbatt, va_0, va_1, va_2, va_3, va_4, va_5, va_6, va_7, va_8, va_9, vf_0, vf_1, vf_2, vf_3, vf_4, vf_5, vf_6, vf_7, vf_8, vf_9 FROM vibracao ORDER BY id DESC LIMIT 4";

// Setar requisição como uma API
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Methods: GET");
header("Access-Control-Max-Age: 3600");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

$response = array();

if ($result = $conn->query($sql)) {
  if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
      foreach ($row as $key => $value) {
        if (!isset($response[$key])) {
          $response[$key] = [];
        }
        $response[$key][] = $value;
      }
    }
    echo json_encode($response);
  } else {
    echo json_encode([]);
  }
  $result->free();
} else {
  echo json_encode([]);
}

$conn->close();
?>
