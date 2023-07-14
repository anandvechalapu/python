package com.sdfasd.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.sdfasd.repository.LoginAuthenticationSystemRepository;
import com.sdfasd.model.LoginAuthenticationSystem;

@Service
public class LoginAuthenticationSystemService {

    @Autowired
    private LoginAuthenticationSystemRepository loginAuthenticationSystemRepository;

    public LoginAuthenticationSystem findByUsernameAndPassword(String username, String password) {
        return loginAuthenticationSystemRepository.findByUsernameAndPassword(username, password);
    }

    public int countByUsername(String username) {
        return loginAuthenticationSystemRepository.countByUsername(username);
    }

    public LoginAuthenticationSystem findByUsername(String username) {
        return loginAuthenticationSystemRepository.findByUsername(username);
    }

    public LoginAuthenticationSystem findByAccessToken(String accessToken) {
        return loginAuthenticationSystemRepository.findByAccessToken(accessToken);
    }

    public LoginAuthenticationSystem findByUsernameAndAccessToken(String username, String accessToken) {
        return loginAuthenticationSystemRepository.findByUsernameAndAccessToken(username, accessToken);
    }

    public void deleteByUsername(String username) {
        loginAuthenticationSystemRepository.deleteByUsername(username);
    }

    public void deleteByAccessToken(String accessToken) {
        loginAuthenticationSystemRepository.deleteByAccessToken(accessToken);
    }

}