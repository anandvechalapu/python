package com.sdfasd.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.sdfasd.entity.User;
import com.sdfasd.service.LoginService;

@RestController
@RequestMapping("/login")
public class LoginController {
	
	@Autowired
	private LoginService loginService;

	@GetMapping("/username/{username}")
	public User findByUsername(@PathVariable String username) {
		return loginService.findByUsername(username);
	}

	@GetMapping("/username/{username}/password/{password}")
	public User findByUsernameAndPassword(@PathVariable String username, @PathVariable String password) {
		return loginService.findByUsernameAndPassword(username, password);
	}

	@PutMapping("/resetpassword")
	public void resetPassword(@RequestBody String username, @RequestBody String newPassword) {
		loginService.resetPassword(username, newPassword);
	}

	@PutMapping("/logout/{username}")
	public void logout(@PathVariable String username) {
		loginService.logout(username);
	}
}