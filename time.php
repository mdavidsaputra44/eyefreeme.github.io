<?php
header('Content-Type: application/json');
echo json_encode([
    'datetime' => gmdate('Y-m-d\TH:i:s.v\Z'),
    'timestamp' => time()
]);
?>
