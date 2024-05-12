/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/qt6/04_arrays.yml
 *   Template: qt6/object_path_header.j2
 */
#pragma once
#include <QObject>
#include <QQmlEngine>
#include <qqmlintegration.h>
#include <QDBusConnection>
#include <QDBusMessage>
#include <memory>
#include "ArraysInterfaceAdaptor.hpp"
#include "ArraysWithStructsInterfaceAdaptor.hpp"
namespace gen::arrays {

/**
 * @brief Container for D-Bus interfaces exposed under the object path "/com/yarpc/testservice/arrays"
 */
class ArraysTestserviceYarpcComObjectPath : public QObject {
    Q_OBJECT
public:
    ArraysTestserviceYarpcComObjectPath(QObject* parent = nullptr);

    /**
     * @brief Returns whether there are any interfaces registered under this object path.
     *
     * @returns whether there are any interfaces registered
     */
    bool hasRegistrations() const;

    /** @brief Pointer to the adaptor for a registered ArraysInterface interface or null if it isn't registered. */
    ArraysInterfaceAdaptor *m_arrays = nullptr;

    /** @brief Pointer to the adaptor for a registered ArraysWithStructsInterface interface or null if it isn't registered. */
    ArraysWithStructsInterfaceAdaptor *m_arraysWithStructs = nullptr;

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
     * @brief Registers the Arrays interface under its object path.
     *
     * @param interface pointer to the Arrays object to register
     */
    void registerArrays(QObject* interface);

    /**
     * @brief Unregisters the Arrays.
     */
    void unregisterArrays();

    /**
     * @brief Returns whether the Arrays interface is registered.
     *
     * @returns whether the interface is registered
     */
    bool isArraysRegistered() const;
    ArraysInterfaceAdaptor * Arrays();

    /**
     * @brief Registers the ArraysWithStructs interface under its object path.
     *
     * @param interface pointer to the ArraysWithStructs object to register
     */
    void registerArraysWithStructs(QObject* interface);

    /**
     * @brief Unregisters the ArraysWithStructs.
     */
    void unregisterArraysWithStructs();

    /**
     * @brief Returns whether the ArraysWithStructs interface is registered.
     *
     * @returns whether the interface is registered
     */
    bool isArraysWithStructsRegistered() const;
    ArraysWithStructsInterfaceAdaptor * ArraysWithStructs();

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

    std::unique_ptr<ArraysTestserviceYarpcComObjectPath> m_ArraysTestserviceYarpcComObjectPath = nullptr;

    QObject* m_Arrays = nullptr;
    QObject* m_ArraysWithStructs = nullptr;

};

}