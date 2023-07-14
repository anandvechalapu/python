package com.sdfasd.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.sdfasd.model.LoginAuthenticationSystem;
import com.sdfasd.service.LoginAuthenticationSystemService;

@RestController
public class LoginAuthenticationSystemController {

    @Autowired
    private LoginAuthenticationSystemService loginAuthenticationSystemService;

    @GetMapping("/login")
    public LoginAuthenticationSystem findByUsernameAndPassword(@RequestParam String username, @RequestParam String password) {
        return loginAuthenticationSystemService.findByUsernameAndPassword(username, password);
    }

    @GetMapping("/countByUsername")
    public int countByUsername(@RequestParam String username) {
        return loginAuthenticationSystemService.countByUsername(username);
    }

    @GetMapping("/findByUsername")
    public LoginAuthenticationSystem findByUsername(@RequestParam String username) {
        return loginAuthenticationSystemService.findByUsername(username);
    }

    @GetMapping("/findByAccessToken")
    public LoginAuthenticationSystem findByAccessToken(@RequestParam String accessToken) {
        return loginAuthenticationSystemService.findByAccessToken(accessToken);
    }

    @GetMapping("/findByUsernameAndAccessToken")
    public LoginAuthenticationSystem findByUsernameAndAccessToken(@RequestParam String username, @RequestParam String accessToken) {
        return loginAuthenticationSystemService.findByUsernameAndAccessToken(username, accessToken);
    }

    @PostMapping("/deleteByUsername")
    public void deleteByUsername(@RequestParam String username) {
        loginAuthenticationSystemService.deleteByUsername(username);
    }

    @PutMapping("/deleteByAccessToken")
    public void deleteByAccessToken(@RequestParam String accessToken) {
        loginAuthenticationSystemService.deleteByAccessToken(accessToken);
    }

}