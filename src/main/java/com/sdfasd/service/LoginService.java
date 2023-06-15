package com.sdfasd.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.sdfasd.entity.User;
import com.sdfasd.repository.LoginRepository;

@Service
public class LoginService {

	@Autowired
	private LoginRepository loginRepository;

	public User findByUsername(String username) {
		return loginRepository.findByUsername(username);
	}

	public User findByUsernameAndPassword(String username, String password) {
		return loginRepository.findByUsernameAndPassword(username, password);
	}

	public void resetPassword(String username, String newPassword) {
		loginRepository.resetPassword(username, newPassword);
	}

	public void logout(String username) {
		loginRepository.logout(username);
	}
}