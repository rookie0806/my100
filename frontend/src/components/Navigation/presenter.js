import React from "react";
import Ionicon from "react-ionicons";
import PropTypes from "prop-types";
import {Router,Link } from "react-router-dom";
import styles from "./styles.module.scss";
import store, { history } from "redux/configureStore";
const Navigation = (props, context) => (
  <div className={styles.navigation}>
    <div className={styles.inner}>
      <div className={styles.column}>
      <Router history={history}>
          <Link to="/">
            <img
              src={require("images/logo.png")}
              className={styles.logo}
              alt={context.t("Logo")}
            />
          </Link>
      </Router>
      </div>
      <div className={styles.column}>
        <form method="post" onSubmit={props.onSubmit}>
          <input
            type="text"
            placeholder={context.t("Search")}
            className={styles.searchInput}
            value={props.value}
            onChange={props.onInputChange}
          />
        </form>
      </div>
      <div className={styles.column}>
        <div className={styles.navIcon}>
          <Router history={history}>
          <Link to="/explore">
            <Ionicon icon="ios-compass-outline" fontSize="28px" color="black" />
          </Link>
          </Router>
        </div>
        <div className={styles.navIcon}>
          <Ionicon icon="ios-heart-outline" fontSize="28px" color="black" />
        </div>
        <div className={styles.navIcon}>
          <Router history={history}>
            <Link to="/profile">
              <Ionicon icon="ios-person-outline" fontSize="32px" color="black" />
            </Link>
          </Router>
        </div>
      </div>
    </div>
  </div>
);

Navigation.propTypes = {
  onInputChange: PropTypes.func.isRequired,
  value: PropTypes.string.isRequired,
  onSubmit: PropTypes.func.isRequired
};

Navigation.contextTypes = {
  t: PropTypes.func.isRequired
};

export default Navigation;
