<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" import="java.util.Date"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
	<title>Time</title>
	<link rel="stylesheet" type="text/css" href="/css/style.css">
	<script type="text/javascript" src="../js/app.js"></script>
</head>
<body>
	<h1><c:out value="${timeString}"/></h1>
</body>
</html>