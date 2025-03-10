/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/qt6/04_arrays.yml
 *   Template: qt6/object_path_source.j2
 */
#include "Connection.hpp"
#include "ArraysInterface.hpp"
#include "ArraysWithStructsInterface.hpp"

using namespace gen::arrays;


ArraysTestserviceYarpcComObjectPath::ArraysTestserviceYarpcComObjectPath(QObject *parent) : QObject(parent) {
}

bool ArraysTestserviceYarpcComObjectPath::hasRegistrations() const {
    return (
        false
        || m_arrays != nullptr
        || m_arraysWithStructs != nullptr
    );
}


Connection::Connection() : QObject(nullptr) {}

Connection& Connection::instance() {
    static Connection object{};
    return object;
}

void Connection::connect() {
    bool hasChanged = false;
    if (m_connection == nullptr) {
        m_connection = std::make_unique<QDBusConnection>(QDBusConnection::connectToBus(QDBusConnection::SessionBus, "com.yarpc.testservice"));
        if ( m_connection->isConnected()) {
            m_connection->registerService("com.yarpc.testservice");
            hasChanged = true;
        }
    }

    if (hasChanged) {
        emit connectedChanged();
    }
}

void Connection::disconnect(){
    if (m_connection == nullptr) {
        return;
    }
    m_connection->disconnectFromBus("com.yarpc.testservice");
    m_connection = nullptr;
    emit connectedChanged();
}

void Connection::disconnectIfUnused(){
    if (
        false
        || m_Arrays != nullptr
        || m_ArraysWithStructs != nullptr
    ) {
        return;
    }
    disconnect();
}

void Connection::updateRegistrations() {
    if (m_connection != nullptr && m_connection->isConnected()) {
        m_connection->unregisterObject("/com/yarpc/testservice/arrays");
        m_ArraysTestserviceYarpcComObjectPath.reset(new ArraysTestserviceYarpcComObjectPath(this));
        if (m_Arrays != nullptr) {
            auto arraysInterface = dynamic_cast<ArraysInterface*>(m_Arrays);
            m_ArraysTestserviceYarpcComObjectPath->m_arrays = new ArraysInterfaceAdaptor(
                arraysInterface,
                m_ArraysTestserviceYarpcComObjectPath.get()
            );
        }
        if (m_ArraysWithStructs != nullptr) {
            auto arraysWithStructsInterface = dynamic_cast<ArraysWithStructsInterface*>(m_ArraysWithStructs);
            m_ArraysTestserviceYarpcComObjectPath->m_arraysWithStructs = new ArraysWithStructsInterfaceAdaptor(
                arraysWithStructsInterface,
                m_ArraysTestserviceYarpcComObjectPath.get()
            );
        }
        if (
            false
            || m_Arrays != nullptr
            || m_ArraysWithStructs != nullptr
        ) {
            m_connection->registerObject(
                "/com/yarpc/testservice/arrays",
                m_ArraysTestserviceYarpcComObjectPath.get()
            );
        }
        emit registrationChanged();
    }
}

bool Connection::getConnected() const {
    return m_connection != nullptr;
}

void Connection::send(const QDBusMessage &message) {
    if (m_connection == nullptr) {
        qDebug() << "Sending message failed: No connection";
        return;
    }
    m_connection->send(message);
}

void Connection::registerArrays(QObject* interface) {
    if (m_Arrays == nullptr) {
        auto arraysInterface = dynamic_cast<ArraysInterface*>(interface);
        if (arraysInterface != nullptr) {
            m_Arrays = interface;
        }
    }
    connect();
    updateRegistrations();
}

void Connection::unregisterArrays() {
    if (m_Arrays != nullptr) {
        m_Arrays = nullptr;
    }
    updateRegistrations();
    disconnectIfUnused();
}

bool Connection::isArraysRegistered() const {
    return (m_Arrays != nullptr);
}

ArraysInterfaceAdaptor* Connection::Arrays() {
    if (m_ArraysTestserviceYarpcComObjectPath != nullptr) {
        return m_ArraysTestserviceYarpcComObjectPath->m_arrays;
    } else {
        return nullptr;
    }
}

void Connection::registerArraysWithStructs(QObject* interface) {
    if (m_ArraysWithStructs == nullptr) {
        auto arraysWithStructsInterface = dynamic_cast<ArraysWithStructsInterface*>(interface);
        if (arraysWithStructsInterface != nullptr) {
            m_ArraysWithStructs = interface;
        }
    }
    connect();
    updateRegistrations();
}

void Connection::unregisterArraysWithStructs() {
    if (m_ArraysWithStructs != nullptr) {
        m_ArraysWithStructs = nullptr;
    }
    updateRegistrations();
    disconnectIfUnused();
}

bool Connection::isArraysWithStructsRegistered() const {
    return (m_ArraysWithStructs != nullptr);
}

ArraysWithStructsInterfaceAdaptor* Connection::ArraysWithStructs() {
    if (m_ArraysTestserviceYarpcComObjectPath != nullptr) {
        return m_ArraysTestserviceYarpcComObjectPath->m_arraysWithStructs;
    } else {
        return nullptr;
    }
}

