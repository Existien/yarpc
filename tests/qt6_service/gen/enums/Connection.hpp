/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/qt6/06_enums.yml
 *   Template: qt6/object_path_header.j2
 */
#pragma once
#include <QObject>
#include <QQmlEngine>
#include <qqmlintegration.h>
#include <QDBusConnection>
#include <QDBusMessage>
#include <memory>
#include "EnumsInterfaceAdaptor.hpp"
namespace gen::enums {

/**
 * @brief Container for D-Bus interfaces exposed under the object path "/com/yarpc/testservice/enums"
 */
class EnumsTestserviceYarpcComObjectPath : public QObject {
    Q_OBJECT
public:
    EnumsTestserviceYarpcComObjectPath(QObject* parent = nullptr);

    /**
     * @brief Returns whether there are any interfaces registered under this object path.
     *
     * @returns whether there are any interfaces registered
     */
    bool hasRegistrations() const;

    /** @brief Pointer to the adaptor for a registered EnumsInterface interface or null if it isn't registered. */
    EnumsInterfaceAdaptor *m_enums = nullptr;

};

/**
 * @brief D-Bus connection singleton.
 *
 * Responsible for managing the registered interfaces
 */
class Connection : public QObject {
Q_OBJECT
/** @brief Whether there are any interfaces registered. */
Q_PROPERTY(bool connected READ getConnected NOTIFY connectedChanged)
public:

    /**
     * @brief Returns the singleton instance.
     *
     * @returns the singleton instance
     */
    static Connection& instance();

    /**
     * @brief Disconnects from the D-Bus if no interfaces are registered.
     */
    void disconnectIfUnused();

    /**
     * @brief Returns whether the a connection to the D-Bus was established.
     *
     * @returns whether a connection was established
     */
    bool getConnected() const;

    /**
     * @brief Send a D-Bus message.
     *
     * @param message the message to send
     */
    void send(const QDBusMessage &message);

    /**
     * @brief Registers the Enums interface under its object path.
     *
     * @param interface pointer to the Enums object to register
     */
    void registerEnums(QObject* interface);

    /**
     * @brief Unregisters the Enums.
     */
    void unregisterEnums();

    /**
     * @brief Returns whether the Enums interface is registered.
     *
     * @returns whether the interface is registered
     */
    bool isEnumsRegistered() const;
    EnumsInterfaceAdaptor * Enums();

public slots:
    /**
     * @brief Establishes a connection to the D-Bus.
     */
    void connect();

    /**
     * @brief Severs a connection to the D-Bus.
     */
    void disconnect();
signals:
    /**
     * @brief Emitted when the connection status changes.
     */
    void connectedChanged();

    /**
     * @brief Emitted when interfaces are registered or unregistered.
     */
    void registrationChanged();
private:
    Connection();

private:
    void updateRegistrations();
    std::unique_ptr<QDBusConnection> m_connection = nullptr;

    std::unique_ptr<EnumsTestserviceYarpcComObjectPath> m_EnumsTestserviceYarpcComObjectPath = nullptr;

    QObject* m_Enums = nullptr;

};

}