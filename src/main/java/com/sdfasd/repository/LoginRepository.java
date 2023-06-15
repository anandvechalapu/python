package com.sdfasd.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.sdfasd.entity.User;

public interface LoginRepository extends JpaRepository<User, Long> {

    User findByUsername(String username);

	User findByUsernameAndPassword(String username, String password);

	void resetPassword(String username, String newPassword);

	void logout(String username);

}