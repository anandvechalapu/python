package com.sdfasd.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface LoginAuthenticationSystemRepository extends JpaRepository<LoginAuthenticationSystem, Long>  {

    public LoginAuthenticationSystem findByUsernameAndPassword(String username, String password);
    public int countByUsername(String username);
    public LoginAuthenticationSystem findByUsername(String username);
    public LoginAuthenticationSystem findByAccessToken(String accessToken);
    public LoginAuthenticationSystem findByUsernameAndAccessToken(String username, String accessToken);
    public void deleteByUsername(String username);
    public void deleteByAccessToken(String accessToken);

}